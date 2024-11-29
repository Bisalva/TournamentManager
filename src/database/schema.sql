-- Tabla Grupos
CREATE TABLE IF NOT EXISTS grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreGrupo TEXT NOT NULL,
    victoriasGrupo INTEGER,
    derrotasGrupo INTEGER
);