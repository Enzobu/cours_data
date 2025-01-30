CREATE TABLE IF NOT EXISTS links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    country_link VARCHAR(255) NOT NULL
);




-- cost_of_life
CREATE TABLE IF NOT EXISTS cost_of_life_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

-- CREATE TABLE IF NOT EXISTS cost_of_life_cleanData (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     country VARCHAR(255) NOT NULL,
--     description TEXT NOT NULL,
--     price FLOAT,
--     unitPrice VARCHAR(255)
-- );


-- crime
CREATE TABLE IF NOT EXISTS crime_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

-- CREATE TABLE IF NOT EXISTS crime_cleanData (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     country VARCHAR(255) NOT NULL,
--     description TEXT NOT NULL,
--     price FLOAT,
--     unitPrice VARCHAR(255)
-- );


-- health_care
CREATE TABLE IF NOT EXISTS health_care_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

-- CREATE TABLE IF NOT EXISTS health_care_cleanData (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     country VARCHAR(255) NOT NULL,
--     description TEXT NOT NULL,
--     price FLOAT,
--     unitPrice VARCHAR(255)
-- );


-- pollution
CREATE TABLE IF NOT EXISTS pollution_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

-- CREATE TABLE IF NOT EXISTS pollution_cleanData (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     country VARCHAR(255) NOT NULL,
--     description TEXT NOT NULL,
--     price FLOAT,
--     unitPrice VARCHAR(255)
-- );


-- quality_of_life
CREATE TABLE IF NOT EXISTS quality_of_life_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

-- CREATE TABLE IF NOT EXISTS quality_of_life_cleanData (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     country VARCHAR(255) NOT NULL,
--     description TEXT NOT NULL,
--     price FLOAT,
--     unitPrice VARCHAR(255)
-- );
