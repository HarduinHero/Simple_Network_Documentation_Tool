-- DeviceType definition

CREATE TABLE DeviceType (
	id_devicetype INTEGER PRIMARY KEY,
	label TEXT NOT NULL UNIQUE
);


-- InterfaceType definition

CREATE TABLE InterfaceType (
	id_interfacetype INTEGER PRIMARY KEY,
	label TEXT NOT NULL UNIQUE
);


-- Metadata definition

CREATE TABLE Metadata (
	creation_date TEXT,
	schema_version TEXT,
	title TEXT,
	description TEXT,
	file_version TEXT
);

INSERT INTO Metadata (creation_date, schema_version, title, description, file_version)
VALUES(strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), '1.1.0', 'Project', 'A new project', '1');


-- Rack definition

CREATE TABLE Rack (
	id_rack INTEGER PRIMARY KEY,
	label_1 TEXT NOT NULL UNIQUE,
	label_2 TEXT,
	height INTEGER,
	description TEXT
);


-- DeviceModel definition

CREATE TABLE DeviceModel (
	id_device_model INTEGER PRIMARY KEY,
	label TEXT NOT NULL,
	file TEXT NOT NULL,
	description TEXT,
	model_device_type INTEGER NOT NULL,
	CONSTRAINT DeviceModel_DeviceType_FK FOREIGN KEY (model_device_type) REFERENCES DeviceType(id_devicetype)
);


-- Device definition

CREATE TABLE Device (
	id_device INTEGER PRIMARY KEY,
	label_1 TEXT NOT NULL,
	label_2 TEXT,
	description TEXT,
	height INTEGER,
	rack_location INTEGER,
	rack_position INTEGER,
	device_model INTEGER NOT NULL,
	CONSTRAINT Device_DeviceModel_FK FOREIGN KEY (device_model) REFERENCES DeviceModel(id_device_model),
	CONSTRAINT device_fk_rack FOREIGN KEY (rack_location) REFERENCES Rack(id_rack)
);


-- Interface definition

CREATE TABLE Interface (
	id_interface INTEGER PRIMARY KEY,
	type_interface INTEGER NOT NULL,
	speeds TEXT,
	label TEXT,
	device INTEGER NOT NULL,
	CONSTRAINT interface_fk_device FOREIGN KEY (device) REFERENCES "Device"(id_device),
	CONSTRAINT interface_fk_interfacetype FOREIGN KEY (type_interface) REFERENCES "InterfaceType"(id_interfacetype)
);


-- Link definition

CREATE TABLE Link (
	interface_a INTEGER NOT NULL,
	interface_b INTEGER NOT NULL,
	physical_color TEXT,
	label TEXT,
	CONSTRAINT link_pk PRIMARY KEY (interface_a, interface_b),
	CONSTRAINT link_fk_interface_a FOREIGN KEY (interface_a) REFERENCES "Interface"(id_interface),
	CONSTRAINT link_fk_interface_b FOREIGN KEY (interface_b) REFERENCES "Interface"(id_interface)
);