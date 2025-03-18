CREATE TABLE IF NOT EXISTS links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    country_link VARCHAR(255) NOT NULL
);


-- cost_of_life
CREATE TABLE IF NOT EXISTS data_cost_of_life (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_cost_of_life (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    unitPrice VARCHAR(255) NOT NULL
);


-- crime
CREATE TABLE IF NOT EXISTS data_crime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_crime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(255) NOT NULL
);


-- health_care
CREATE TABLE IF NOT EXISTS data_health_care (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_health_care (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(255) NOT NULL
);


-- pollution
CREATE TABLE IF NOT EXISTS data_pollution (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_pollution (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(255) NOT NULL
);


-- quality_of_life
CREATE TABLE IF NOT EXISTS data_quality_of_life (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_quality_of_life (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(255) NOT NULL
);


-- data_crime_index
CREATE TABLE IF NOT EXISTS data_crime_index (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    crime_index TEXT,
);

CREATE TABLE IF NOT EXISTS clean_data_crime_index (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    crime_index TEXT NOT NULL,
);


-- matrix_cost_of_life
CREATE TABLE matrix_cost_of_life (
    country VARCHAR(255),
    meal_inexpensive FLOAT,
    meal_for_two FLOAT,
    mcmeal FLOAT,
    domestic_beer FLOAT,
    imported_beer FLOAT,
    cappuccino FLOAT,
    coke_pepsi FLOAT,
    water_small FLOAT,
    milk FLOAT,
    bread FLOAT,
    rice FLOAT,
    eggs FLOAT,
    cheese FLOAT,
    chicken FLOAT,
    beef FLOAT,
    apples FLOAT,
    banana FLOAT,
    oranges FLOAT,
    tomato FLOAT,
    potato FLOAT,
    onion FLOAT,
    lettuce FLOAT,
    water_large FLOAT,
    non_alcoholic_wine FLOAT,
    cigarettes FLOAT,
    local_transport_ticket FLOAT,
    monthly_pass FLOAT,
    taxi_start FLOAT,
    taxi_per_km FLOAT,
    taxi_waiting FLOAT,
    gasoline FLOAT,
    volkswagen_golf FLOAT,
    toyota_corolla FLOAT,
    utilities FLOAT,
    mobile_plan FLOAT,
    internet FLOAT,
    fitness_club FLOAT,
    tennis_court FLOAT,
    cinema FLOAT,
    preschool FLOAT,
    primary_school FLOAT,
    jeans FLOAT,
    summer_dress FLOAT,
    nike_shoes FLOAT,
    leather_shoes FLOAT,
    apt_1bed_city FLOAT,
    apt_1bed_out FLOAT,
    apt_3bed_city FLOAT,
    apt_3bed_out FLOAT,
    price_sq_m_city FLOAT,
    price_sq_m_out FLOAT,
    net_salary FLOAT,
    crime_index FLOAT
);
