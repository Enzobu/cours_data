from db.getConn import getConn

def flushMatrix(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        crime_index = row['crime_index']
        meal_inexpensive = row['meal_inexpensive']
        meal_for_two = row['meal_for_two']
        mcmeal = row['mcmeal']
        domestic_beer = row['domestic_beer']
        imported_beer = row['imported_beer']
        cappuccino = row['cappuccino']
        coke_pepsi = row['coke_pepsi']
        water_small = row['water_small']
        milk = row['milk']
        bread = row['bread']
        rice = row['rice']
        eggs = row['eggs']
        cheese = row['cheese']
        chicken = row['chicken']
        beef = row['beef']
        apples = row['apples']
        banana = row['banana']
        oranges = row['oranges']
        tomato = row['tomato']
        potato = row['potato']
        onion = row['onion']
        lettuce = row['lettuce']
        water_large = row['water_large']
        non_alcoholic_wine = row['non_alcoholic_wine']
        cigarettes = row['cigarettes']
        local_transport_ticket = row['local_transport_ticket']
        monthly_pass = row['monthly_pass']
        taxi_start = row['taxi_start']
        taxi_per_km = row['taxi_per_km']
        taxi_waiting = row['taxi_waiting']
        gasoline = row['gasoline']
        volkswagen_golf = row['volkswagen_golf']
        toyota_corolla = row['toyota_corolla']
        utilities = row['utilities']
        mobile_plan = row['mobile_plan']
        internet = row['internet']
        fitness_club = row['fitness_club']
        tennis_court = row['tennis_court']
        cinema = row['cinema']
        preschool = row['preschool']
        primary_school = row['primary_school']
        jeans = row['jeans']
        summer_dress = row['summer_dress']
        nike_shoes = row['nike_shoes']
        leather_shoes = row['leather_shoes']
        apt_1bed_city = row['apt_1bed_city']
        apt_1bed_out = row['apt_1bed_out']
        apt_3bed_city = row['apt_3bed_city']
        apt_3bed_out = row['apt_3bed_out']
        price_sq_m_city = row['price_sq_m_city']
        price_sq_m_out = row['price_sq_m_out']
        net_salary = row['net_salary']
        
        sql = """
        INSERT INTO matrix_cost_of_life (
            country, meal_inexpensive, meal_for_two, mcmeal, domestic_beer, imported_beer, 
            cappuccino, coke_pepsi, water_small, milk, bread, rice, eggs, cheese, chicken, 
            beef, apples, banana, oranges, tomato, potato, onion, lettuce, water_large, 
            non_alcoholic_wine, cigarettes, local_transport_ticket, monthly_pass, taxi_start, 
            taxi_per_km, taxi_waiting, gasoline, volkswagen_golf, toyota_corolla, utilities, 
            mobile_plan, internet, fitness_club, tennis_court, cinema, preschool, primary_school, 
            jeans, summer_dress, nike_shoes, leather_shoes, apt_1bed_city, apt_1bed_out, 
            apt_3bed_city, apt_3bed_out, price_sq_m_city, price_sq_m_out, net_salary, crime_index
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            country, meal_inexpensive, meal_for_two, mcmeal, domestic_beer, imported_beer, 
            cappuccino, coke_pepsi, water_small, milk, bread, rice, eggs, cheese, chicken, 
            beef, apples, banana, oranges, tomato, potato, onion, lettuce, water_large, 
            non_alcoholic_wine, cigarettes, local_transport_ticket, monthly_pass, taxi_start, 
            taxi_per_km, taxi_waiting, gasoline, volkswagen_golf, toyota_corolla, utilities, 
            mobile_plan, internet, fitness_club, tennis_court, cinema, preschool, primary_school, 
            jeans, summer_dress, nike_shoes, leather_shoes, apt_1bed_city, apt_1bed_out, 
            apt_3bed_city, apt_3bed_out, price_sq_m_city, price_sq_m_out, net_salary, crime_index
        )

        cursor.execute(sql, data)


    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_cost_of_life.")