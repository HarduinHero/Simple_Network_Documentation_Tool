ALTER TABLE public."Rack" ADD id_rack uuid NOT NULL;

ALTER TABLE public."Interface" ADD device uuid NOT NULL;

ALTER TABLE public."Interface" ADD type_interface int4 NOT NULL;

ALTER TABLE public."Device" ADD height varchar NULL;

ALTER TABLE public."Device" ADD "type" int4 NULL;

-- Drop table

-- DROP TABLE "Link";

CREATE TABLE "Link" (
	interface_a uuid NOT NULL,
	interface_b uuid NOT NULL,
	physical_color varchar NULL,
	"label" varchar NULL,
	CONSTRAINT link_pk PRIMARY KEY (interface_a, interface_b),
	CONSTRAINT link_fk_interface_a FOREIGN KEY (interface_a) REFERENCES "Interface"(id_interface),
	CONSTRAINT link_fk_interface_b FOREIGN KEY (interface_b) REFERENCES "Interface"(id_interface)
);

ALTER TABLE public."Rack" ADD description varchar NULL;

ALTER TABLE public."Device" ADD label_1 varchar NOT NULL;

-- Drop table

-- DROP TABLE "DeviceType";

CREATE TABLE "DeviceType" (
	id_devicetype serial4 NOT NULL,
	"label" varchar NULL,
	CONSTRAINT devicetype_pk PRIMARY KEY (id_devicetype)
);

ALTER TABLE public."Interface" ADD speeds varchar NULL;

ALTER TABLE public."Link" ADD interface_b uuid NOT NULL;

ALTER TABLE public."Link" ADD "label" varchar NULL;

ALTER TABLE public."Link" ADD physical_color varchar NULL;

ALTER TABLE public."Device" ADD description varchar NULL;

-- Drop table

-- DROP TABLE "Interface";

CREATE TABLE "Interface" (
	id_interface uuid NOT NULL,
	type_interface int4 NOT NULL,
	speeds varchar NULL,
	"label" varchar NULL,
	device uuid NOT NULL,
	CONSTRAINT interface_pk PRIMARY KEY (id_interface),
	CONSTRAINT interface_fk_device FOREIGN KEY (device) REFERENCES "Device"(id_device),
	CONSTRAINT interface_fk_interfacetype FOREIGN KEY (type_interface) REFERENCES "InterfaceType"(id_interfacetype)
);

ALTER TABLE public."Device" ADD label_2 varchar NULL;

ALTER TABLE public."DeviceType" ADD id_devicetype serial4 NOT NULL;

ALTER TABLE public."Device" ADD id_device uuid NOT NULL;

ALTER TABLE public."Link" ADD interface_a uuid NOT NULL;

ALTER TABLE public."Rack" ADD height int2 NOT NULL;

ALTER TABLE public."Interface" ADD "label" varchar NULL;

ALTER TABLE public."InterfaceType" ADD id_interfacetype serial4 NOT NULL;

-- Drop table

-- DROP TABLE "Device";

CREATE TABLE "Device" (
	id_device uuid NOT NULL,
	label_1 varchar NOT NULL,
	label_2 varchar NULL,
	description varchar NULL,
	height varchar NULL,
	rack_location uuid NULL,
	rack_position int4 NULL,
	"type" int4 NULL,
	CONSTRAINT device_pk PRIMARY KEY (id_device),
	CONSTRAINT device_fk_devicetype FOREIGN KEY ("type") REFERENCES "DeviceType"(id_devicetype),
	CONSTRAINT device_fk_rack FOREIGN KEY (rack_location) REFERENCES "Rack"(id_rack)
);

ALTER TABLE public."Device" ADD rack_position int4 NULL;

ALTER TABLE public."Interface" ADD id_interface uuid NOT NULL;

ALTER TABLE public."Rack" ADD label_2 varchar NULL;

ALTER TABLE public."InterfaceType" ADD "label" varchar NULL;

-- Drop table

-- DROP TABLE "InterfaceType";

CREATE TABLE "InterfaceType" (
	id_interfacetype serial4 NOT NULL,
	"label" varchar NULL,
	CONSTRAINT interfacetype_pk PRIMARY KEY (id_interfacetype)
);

-- Drop table

-- DROP TABLE "Rack";

CREATE TABLE "Rack" (
	id_rack uuid NOT NULL,
	label_1 varchar NOT NULL,
	label_2 varchar NULL,
	height int2 NOT NULL,
	description varchar NULL,
	CONSTRAINT rack_pk PRIMARY KEY (id_rack),
	CONSTRAINT rack_un UNIQUE (label_1)
);

ALTER TABLE public."DeviceType" ADD "label" varchar NULL;

ALTER TABLE public."Device" ADD rack_location uuid NULL;

ALTER TABLE public."Rack" ADD label_1 varchar NOT NULL;
