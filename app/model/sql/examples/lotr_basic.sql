-- Lord of the ring (basic)

UPDATE Metadata
SET title='Lord Of The Ring basic example', description='A basic example from the hobbits.'
WHERE _ROWID_ = 1;

INSERT INTO DeviceType
	(label)
	VALUES ('Personal computer'), ('Switch'), ('Printer'), ('Patch panel'), ('Server');
	
INSERT INTO InterfaceType
	(label)
	VALUES ('Ethernet'), ('SFP');
	
INSERT INTO Rack 
	(label_1, label_2, height, description) VALUES
	('R-001', 'Bucklebury-001', 10, ''),
	('R-201', 'Bucklebury-002',  5, '');

INSERT INTO DeviceModel 
	(label, file, description, model_device_type)
	VALUES ('Generic computer', 'generic_computer_1eth1Gb.json', 'Placeholder model for a computer (1eth1Gb)', 1),
		   ('Generic swith 5-1c', 'generic_switch_5*eth1Gb_1*sfp1GbCombo.json', 'Placeholder model for a simple switch (5*eth1Gb + 1*sfp1GbCombo)', 2),
		   ('Generic printer', 'generic_printer_1eth1Gb.json', 'Placeholder model for a printer (1eth1Gb)', 3),
		   ('Generic patch panel', 'generic_patch_panel_5*eth1Gb.json', 'Placeholder model for a patch panel (5*eth1Gb)', 4),
		   ('Generic server', 'generic_server_1*eth1Gb_1*sfp10Gb.json', 'Placeholder model for a simple server (1*eth1Gb + 1*sfp10Gb)', 5);
	
INSERT INTO Device 
	(label_1, label_2, description, height, rack_location, rack_position, device_model)
	VALUES ('PC1', "Frodo's workstation",  '', NULL, NULL, NULL, 1),
		   ('PC2', "Sam's workstation",    '', NULL, NULL, NULL, 1),
		   ('PC3', "Pippin's workstation", '', NULL, NULL, NULL, 1),
		   ('PC4', "Merry's workstation",  '', NULL, NULL, NULL, 1),
		   ('PC5', "Bilbo's workstation",  '', NULL, NULL, NULL, 1),
		   ('SW1', '', '', 1, 1, 3, 2),
		   ('SW2', '', '', 1, 2, 4, 2),
		   ('Printer 1', '1st floor printer', '', NULL, NULL, NULL, 3),
		   ('Printer 2', '2nd floor printer', '', NULL, NULL, NULL, 3),
		   ('Ptch1', '', '', 1, 1, 1, 4),
		   ('Ptch2', '', '', 1, 2, 1, 4),
		   ('SERV', "Bag End's file server", '', 2, 1, 4, 5);
		   
INSERT INTO Interface
	(label, type_interface, speeds, device)
	VALUES ('1', 1, '10/100/1000', 1),
		   ('1', 1, '10/100/1000', 2),
		   ('1', 1, '10/100/1000', 3),
		   ('1', 1, '10/100/1000', 4),
		   ('1', 1, '10/100/1000', 5),
		   ('1', 1, '10/100/1000', 6),
		   ('2', 1, '10/100/1000', 6),
		   ('3', 1, '10/100/1000', 6),
		   ('4', 1, '10/100/1000', 6),
		   ('5', 1, '10/100/1000', 6),
		   ('5', 2, '10/100/1000', 6),
		   ('1', 1, '10/100/1000', 7),
		   ('2', 1, '10/100/1000', 7),
		   ('3', 1, '10/100/1000', 7),
		   ('4', 1, '10/100/1000', 7),
		   ('5', 1, '10/100/1000', 7),
		   ('5', 2, '10/100/1000', 7),
		   ('1', 1, '10/100/1000', 8),
		   ('1', 1, '10/100/1000', 9),
		   ('1', 1, '10/100/1000', 10),
		   ('2', 1, '10/100/1000', 10),
		   ('3', 1, '10/100/1000', 10),
		   ('4', 1, '10/100/1000', 10),
		   ('5', 1, '10/100/1000', 10),
		   ('1', 1, '10/100/1000', 11),
		   ('2', 1, '10/100/1000', 11),
		   ('3', 1, '10/100/1000', 11),
		   ('4', 1, '10/100/1000', 11),
		   ('5', 1, '10/100/1000', 11),
		   ('1', 1, '10/100/1000', 12),
		   ('2', 2, '1000/10000',  12);
		  
INSERT INTO Link
	(interface_a, interface_b, label, physical_color)
	VALUES (6, 20, NULL, 'white'),
	(7, 21, NULL, 'white'),
	(8, 22, NULL, 'white'),
	(9, 30, NULL, 'white'),
	(11, 17, NULL, 'red'),
	(20, 1, NULL, NULL),
	(21, 2, NULL, NULL),
	(22, 18, NULL, 'green'),
	(12, 25, NULL, NULL),
	(13, 26, NULL, NULL),
	(14, 27, NULL, NULL),
	(15, 28, NULL, NULL),
	(25, 3, NULL, NULL),
	(26, 4, NULL, NULL),
	(27, 19, NULL, NULL),
	(28, 5, NULL, 'green');