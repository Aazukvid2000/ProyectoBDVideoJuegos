import pandas as pd
from sqlalchemy import create_engine, text
import os

# Configuración de la conexión a la base de datos (usamos la misma del proyecto)
DATABASE_URL = "mysql+pymysql://root:rootpassword@db:3306/video_games"
engine = create_engine(DATABASE_URL)

def get_top_generos_juegos(TOP):
    """
    Obtiene los TOP géneros de juegos más populares basado en cantidad de juegos
    """
    query = f"""
    SELECT g.genre_name as 'Género', 
           COUNT(ga.id) as 'Cantidad'
    FROM genre g
    JOIN game ga ON g.id = ga.genre_id
    GROUP BY g.genre_name
    ORDER BY COUNT(ga.id) DESC
    LIMIT {TOP}
    """
    
    df = pd.read_sql(query, engine)
    return df

def get_top_juegos_menos_ventas(TOP):
    """
    Obtiene los TOP juegos con menos ventas totales
    """
    query = f"""
    SELECT ga.game_name as 'Juego', 
           COALESCE(SUM(rs.num_sales), 0) as 'Ventas Totales'
    FROM game ga
    LEFT JOIN game_publisher gp ON ga.id = gp.game_id
    LEFT JOIN game_platform gpl ON gp.id = gpl.game_publisher_id
    LEFT JOIN region_sales rs ON gpl.id = rs.game_platform_id
    GROUP BY ga.game_name
    ORDER BY COALESCE(SUM(rs.num_sales), 0) ASC
    LIMIT {TOP}
    """
    
    df = pd.read_sql(query, engine)
    return df

def get_top_publishers_juegos(TOP):
    """
    Obtiene los TOP publishers con más juegos publicados
    """
    query = f"""
    SELECT p.publisher_name as 'Nombre de la editorial', 
           COUNT(DISTINCT gp.game_id) as 'Cantidad de Juegos'
    FROM publisher p
    JOIN game_publisher gp ON p.id = gp.publisher_id
    GROUP BY p.publisher_name
    ORDER BY COUNT(DISTINCT gp.game_id) DESC
    LIMIT {TOP}
    """
    
    df = pd.read_sql(query, engine)
    return df