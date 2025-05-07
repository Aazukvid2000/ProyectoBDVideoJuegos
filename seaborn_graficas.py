from fastapi import Response
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from sqlalchemy import create_engine, text

# Configuración de la conexión a la base de datos
DATABASE_URL = "mysql+pymysql://root:rootpassword@db:3306/video_games"
engine = create_engine(DATABASE_URL)

def get_top_juegos_ventas(TOP):
    """
    Genera una gráfica de barras con los TOP juegos con mayores ventas
    """
    query = f"""
    SELECT ga.game_name as title, 
           SUM(rs.num_sales) as revenue
    FROM game ga
    JOIN game_publisher gp ON ga.id = gp.game_id
    JOIN game_platform gpl ON gp.id = gpl.game_publisher_id
    JOIN region_sales rs ON gpl.id = rs.game_platform_id
    GROUP BY ga.game_name
    ORDER BY SUM(rs.num_sales) DESC
    LIMIT {TOP}
    """
    
    df = pd.read_sql(query, engine)
    
    plt.figure(figsize=(max(10, len(df)*0.8), 6))
    grafica = sns.barplot(x='title', y='revenue', data=df, palette='deep')
    
    plt.title(f"TOP {TOP} juegos con mayores ventas")
    plt.ylabel("VENTAS (EN MILLONES)")
    plt.xlabel("JUEGOS")
    grafica.set_xticklabels(grafica.get_xticklabels(), rotation=10, ha='right')
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return Response(content=buffer.read(), media_type="image/png")

def get_top_generos_ventas(TOP):
    """
    Genera una gráfica de pastel con los TOP géneros con mayores ventas
    """
    if TOP > 20:
        return "El número dado excede el número de géneros disponibles"
    
    query = f"""
    SELECT g.genre_name, 
           SUM(rs.num_sales) as total_sales
    FROM genre g
    JOIN game ga ON g.id = ga.genre_id
    JOIN game_publisher gp ON ga.id = gp.game_id
    JOIN game_platform gpl ON gp.id = gpl.game_publisher_id
    JOIN region_sales rs ON gpl.id = rs.game_platform_id
    GROUP BY g.genre_name
    ORDER BY SUM(rs.num_sales) DESC
    LIMIT {TOP}
    """
    
    df = pd.read_sql(query, engine)
    
    plt.figure(figsize=(19, 13))
    plt.pie(df['total_sales'].values, autopct=lambda p: f'{p:.1f}%', startangle=150, colors=plt.cm.Paired.colors)
    plt.legend([f"{genre} ({count:.1f}M)" for genre, count in zip(df['genre_name'], df['total_sales'])], loc="best")
    plt.axis('equal')
    plt.title(f"TOP {TOP} géneros con mayores ventas")
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return Response(content=buffer.read(), media_type="image/png")

def get_ventas_plataforma_region(TOP):
    """
    Genera una gráfica de barras apiladas con los TOP plataformas 
    y sus ventas por región
    """
    query = f"""
    SELECT p.platform_name as title, 
           r.region_name as region,
           SUM(rs.num_sales) as ventas
    FROM platform p
    JOIN game_platform gp ON p.id = gp.platform_id
    JOIN region_sales rs ON gp.id = rs.game_platform_id
    JOIN region r ON rs.region_id = r.id
    GROUP BY p.platform_name, r.region_name
    ORDER BY SUM(rs.num_sales) DESC
    """
    
    df = pd.read_sql(query, engine)
    
    # Pivotear los datos para obtener regiones como columnas
    pivot_df = df.pivot_table(index='title', columns='region', values='ventas', aggfunc='sum')
    
    # Ordenar por ventas totales y tomar TOP
    pivot_df['total'] = pivot_df.sum(axis=1)
    pivot_df = pivot_df.sort_values('total', ascending=False).head(TOP)
    pivot_df = pivot_df.drop('total', axis=1)
    
    fig, ax = plt.subplots(figsize=(19, 13))
    ax.set_xlabel("Plataforma")
    ax.set_ylabel("Ventas (en millones)")
    
    # Crear la paleta de colores
    dark_center_div = sns.diverging_palette(150, 275, s=80, l=55, n=pivot_df.shape[1], center="dark")
    
    # Crear la gráfica de barras apiladas
    pivot_df.plot(kind='bar', stacked=True, ax=ax, color=dark_center_div)
    
    plt.xticks(rotation=15, ha='right')
    plt.title(f"TOP {TOP} plataformas por ventas en cada región")
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return Response(content=buffer.read(), media_type="image/png")