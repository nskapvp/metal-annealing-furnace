CREATE TABLE stage
(ID SERIAL PRIMARY KEY,
time_ustavka REAL NOT NULL,
temperature_ustavka REAL NOT NULL,
gas REAL NOT NULL,
pressure REAL NOT NULL
);

CREATE TABLE recipe
(ID SERIAL PRIMARY KEY,
name_recipe VARCHAR(30) NOT NULL,
stage_1_id INTEGER NOT NULL,
stage_2_id INTEGER NOT NULL,
stage_3_id INTEGER NOT NULL,
stage_4_id INTEGER NOT NULL,
stage_5_id INTEGER NOT NULL,
FOREIGN KEY(stage_1_id) REFERENCES stage(ID),
FOREIGN KEY(stage_2_id) REFERENCES stage(ID),
FOREIGN KEY(stage_3_id) REFERENCES stage(ID),
FOREIGN KEY(stage_4_id) REFERENCES stage(ID),
FOREIGN KEY(stage_5_id) REFERENCES stage(ID)
);

INSERT INTO stage (time_ustavka, temperature_ustavka, gas, pressure) VALUES
(1.0, 100.0, 10.0, 1.0),
(2.0, 200.0, 20.0, 2.0),
(3.0, 300.0, 30.0, 3.0),
(4.0, 400.0, 40.0, 4.0),
(5.0, 500.0, 50.0, 5.0);
INSERT INTO recipe (name_recipe, stage_1_id, stage_2_id, stage_3_id, stage_4_id, stage_5_id) VALUES
('Test Recipe', 1, 2, 3, 4, 5);

INSERT INTO stage (time_ustavka, temperature_ustavka, gas, pressure) VALUES
(2.0, 100.0, 5.0, 10.0),
(4.0, 200.0, 7.0, 10.0),
(5.0, 600.0, 10.0, 10.0),
(5.0, 600.0, 10.0, 10.0),
(3.0, 300.0, 10.0, 10.0);
INSERT INTO recipe (name_recipe, stage_1_id, stage_2_id, stage_3_id, stage_4_id, stage_5_id) VALUES
('Recipe 2', 6, 7, 8, 9, 10);

INSERT INTO stage (time_ustavka, temperature_ustavka, gas, pressure) VALUES
(2.0, 100.0, 5.0, 10.0),
(4.0, 200.0, 7.0, 10.0),
(5.0, 650.0, 10.0, 10.0),
(5.0, 700.0, 10.0, 10.0),
(3.0, 800.0, 10.0, 10.0);
INSERT INTO recipe (name_recipe, stage_1_id, stage_2_id, stage_3_id, stage_4_id, stage_5_id) VALUES
('Recipe 3', 11, 12, 13, 14, 15);

INSERT INTO stage (time_ustavka, temperature_ustavka, gas, pressure) VALUES
(120.0, 100.0, 5.0, 10.0),
(240.0, 200.0, 7.0, 10.0),
(300.0, 650.0, 10.0, 10.0),
(300.0, 700.0, 10.0, 10.0),
(180.0, 800.0, 10.0, 10.0);
INSERT INTO recipe (name_recipe, stage_1_id, stage_2_id, stage_3_id, stage_4_id, stage_5_id) VALUES
('Recipe 4', 16, 17, 18, 19, 20);

SELECT * FROM stage;
SELECT * FROM recipe;

TRUNCATE stage, recipe;

DROP TABLE stage;
DROP TABLE recipe;