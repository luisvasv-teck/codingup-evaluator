CREATE TABLE IF NOT EXISTS teachers (
    id_teacher  TEXT NOT NULL,
    full_name   TEXT NOT NULL,
    email       TEXT NOT NULL,
    active      INTEGER NOT NULL,
    CONSTRAINT chk_email CHECK (
        email LIKE '%_@_%._%'
        AND LENGTH(email) - LENGTH(REPLACE(email, '@', '')) = 1
        AND SUBSTR(LOWER(email), 1, INSTR(email, '.') - 1) NOT GLOB '*[^@0-9a-z]*'
        AND SUBSTR(LOWER(email), INSTR(email, '.') + 1) NOT GLOB '*[^a-z]*'
    ),
    PRIMARY KEY(id_teacher)
);