DROP TABLE IF EXISTS "Link";
DROP TABLE IF EXISTS "Device";
DROP TABLE IF EXISTS "Rack";

CREATE TABLE "Rack" (
	id_rack uuid NOT NULL,
	technical_label varchar NOT NULL,
	common_label varchar NULL,
	size_u int2 NOT NULL,
	description varchar NULL,
	CONSTRAINT baie_check CHECK ((size_u >= 0)),
	CONSTRAINT baie_pk PRIMARY KEY (id_rack),
	CONSTRAINT baie_unique_tech_label UNIQUE (technical_label)
);

CREATE TABLE "Device" (
	id_device uuid NOT NULL,
	technical_label varchar NOT NULL,
	common_label varchar NULL,
	description varchar NULL,
	size_u int2 NULL,
	"location" uuid NULL,
	position_u int2 NULL,
	"template" uuid NOT NULL, -- Référence à un fichier de conf xml
	CONSTRAINT device_check CHECK ((position_u >= 0)),
	CONSTRAINT device_check_size_positive CHECK ((size_u >= 0)),
	CONSTRAINT device_pk PRIMARY KEY (id_device),
	CONSTRAINT device_unique UNIQUE (technical_label),
	CONSTRAINT location_rack_fk FOREIGN KEY ("location") REFERENCES "Rack"(id_rack) ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE "Link" (
	device_a uuid NOT NULL,
	device_b uuid NOT NULL,
	port_a int2 NOT NULL,
	port_b int2 NOT NULL,
	CONSTRAINT link_pk PRIMARY KEY (device_a, device_b, port_a, port_b),
	CONSTRAINT link_device_a_fk FOREIGN KEY (device_a) REFERENCES "Device"(id_device) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT link_device_b_fk FOREIGN KEY (device_b) REFERENCES "Device"(id_device) ON DELETE RESTRICT ON UPDATE RESTRICT
);