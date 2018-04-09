PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT);
INSERT INTO "students" VALUES('Alj','Sua','Naga','4400');
INSERT INTO "students" VALUES('alj2','none','NAGA','');
INSERT INTO "students" VALUES('MArco','','Pili','4405');
INSERT INTO "students" VALUES('The Phoenix','West Blue','','12334545');
COMMIT;
