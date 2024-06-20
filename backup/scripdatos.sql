create database maquinaria_cmms;
use maquinaria_cmms;

# Roles
INSERT INTO usuario_rol(rol, estado) VALUES('Asistente',1), ('Admin',1), ('Supervisor',1), ('Gerencia',1),('Mecanico',1);

# CECO
select * from ceco_ceco;
INSERT INTO ceco_ceco(ceco, estado) VALUES('CECO-001',1),('CECO-002',1);

# Sedes
INSERT INTO localizacion_sede(sede, estado) VALUES('Chincha', 1), ('Ica',1);

# Fundos
select * from fundo_cultivo_fundo;
INSERT INTO fundo_cultivo_fundo (fundo, estado, idsede_id) VALUES
('Fortuna', 1, 2),
('San Isidro', 1, 2),
('Alpine 511', 1, 2),
('Alpine Peru', 1, 2),
('Luren', 1, 2),
('Karla', 1, 2),
('Gloria', 1, 2),
('San Hilarion', 1, 2);

# Cultivo
INSERT INTO fundo_cultivo_cultivo(cultivo, estado) VALUES 
('Esparrago', 1),
('Vid', 1),
('Arandanos', 1),
('Granada', 1),
('Arandano', 1),
('Mandarina', 1),
('Pecano', 1),
('Cerezo', 1),
('Palto', 1),
('Taller-Vid', 1),
('Taller-Maestranza', 1);

# TIPO SOLICITANTE
INSERT INTO operarios_tiposolicitante(tiposolicitante, estado) VALUES('Jefe Fundo', 1),('Jefe de Sanidad', 1);

# Cultivo
INSERT INTO fundo_cultivo_cultivo(cultivo, estado) VALUES 
('Esparrago', 1),
('Arandanos', 1),
('Granada', 1),
('Pecano', 1),
('Palto', 1);

# variedad
INSERT INTO fundo_cultivo_variedad(variedad, estado, idcultivo_id) VALUES 
('Gijnlim', 1, 1), ('Atlas', 1, 1), ('Purple Passion', 1, 1),
('Bluecrop', 1, 2), ('Duke', 1, 2), ('Legacy', 1, 2),
('Wonderful', 1, 3), ('Angel Red', 1, 3), ('Parfianka', 1, 3),
('Desirable', 1, 4), ('Stuart', 1, 4), ('Cape Fear', 1, 4),
('Hass', 1, 5), ('Fuerte', 1, 5), ('Pinkerton', 1, 5);

#lote
INSERT INTO fundo_cultivo_lote(lote, estado, idfundo_id,idvariedad_id) values
('10001',1,1,1),
('10002',1,1,2),
('10003',1,2,3),
('10004',1,2,4),
('10005',1,3,5),
('10006',1,3,6),
('10007',1,4,7),
('10008',1,4,8),
('10009',1,5,9),
('10010',1,5,10),
('10011',1,6,11),
('10012',1,6,12),
('10013',1,7,13),
('10014',1,7,14),
('10015',1,8,15),
('10016',1,8,15);

# Personas
INSERT INTO usuario_persona (nombres, apellidos, dni, codigo, estado) VALUES
('Carlos', 'Gómez', '12345678', '10000', 1),
('María', 'Pérez', '87654321', '10001', 1),
('Luis', 'Rodríguez', '11223344', '10002', 1),
('Ana', 'López', '44332211', '10003', 1),
('Jorge', 'Martínez', '55667788', '10004', 1),
('Elena', 'García', '99887766', '10005', 1),
('Pedro', 'Fernández', '66778899', '10006', 1),
('Laura', 'Sánchez', '33445566', '10007', 1),
('Juan', 'Ramírez', '77889900', '10008', 1),
('Marta', 'Torres', '44556677', '10009', 1),
('Fernando', 'Hernández', '22334455', '10010', 1),
('Isabel', 'Ruiz', '99887711', '10011', 1),
('Ricardo', 'Jiménez', '55443322', '10012', 1),
('Sofía', 'Mendoza', '66778822', '10013', 1),
('Alberto', 'Vargas', '22113344', '10014', 1),
('Gabriela', 'Castro', '33445511', '10015', 1),
('Tomás', 'Romero', '77889933', '10016', 1),
('Patricia', 'Ortega', '55667799', '10017', 1),
('Héctor', 'Gil', '11224433', '10018', 1),
('Lucía', 'Flores', '88990077','10019', 1);

# Tractoristas
select * from operarios_tractorista;
INSERT INTO operarios_tractorista(estado, estado_actividad, idpersona_id, idusuario_id) VALUES 
(1, 1, 1,2),
(1, 1, 2,2),
(1, 1, 3,2),
(1, 1, 4,2),
(1, 1, 5,2);

INSERT INTO operarios_tractorista(estado, estado_actividad, idpersona_id, idusuario_id) VALUES 
(1, 1, 11, 3),
(1, 1, 12, 3),
(1, 1, 13, 3),
(1, 1, 14, 3),
(1, 1, 15, 3);

# Solicitantes
INSERT INTO operarios_solicitante(estado, estado_actividad, idpersona_id, idtiposolicitante_id) VALUES
(1,1,6,1),
(1,1,7,1),
(1,1,8,2),
(1,1,9,2),
(1,1,10,1),
(1,1,16,2),
(1,1,17,2),
(1,1,18,2),
(1,1,19,2),
(1,1,20,2);

#Sistemas
INSERT INTO componente_pieza_sistema (sistema, estado)
VALUES
('Eléctrico', 1),
('Mecánico', 1),
('Hidráulico', 1),
('Neumático', 1);

#Componentes
INSERT INTO componente_pieza_componente (idsistema_id, componente, codcomponente, tiempovida, frecuencia_man, estado, creado_en)
VALUES
(1, 'Motor Eléctrico', 'C001', 2000, 500, 1, now()),
(1, 'Generador', 'C002', 2000, 500, 1, now()),
(2, 'Torno', 'C003', 2000, 500, 1, now()),
(2, 'Fresadora', 'C004', 2000, 500, 1, now()),
(3, 'Bomba Hidráulica', 'C005', 2000, 500, 1, now()),
(3, 'Válvula', 'C006', 2000, 500, 1, now()),
(4, 'Compresor', 'C007', 2000, 500, 1, now()),
(4, 'Cilindro Neumático', 'C008', 2000, 500, 1, now()),
(1, 'Transformador', 'C009', 2000, 500, 1, now()),
(2, 'Taladro', 'C010', 2000, 500, 1, now());

#Pieza
INSERT INTO componente_pieza_pieza (pieza, codpieza, frecuencia_man, tiempovida, estado, creado_en) VALUES
('Bobina', 'P001', 500, 2000, 1, NOW()),
('Rotor', 'P002', 500, 2000, 1,  NOW()),
('Estator', 'P003', 500, 2000, 1,NOW()),
('Carcasa', 'P004', 500, 2000, 1, NOW()),
('Cuchilla', 'P005', 500, 2000, 1, NOW()),
('Mandril', 'P006', 500, 2000, 1, NOW()),
('Mesa', 'P007', 500, 2000, 1, NOW()),
('Cabezal', 'P008', 500, 2000, 1, NOW()),
('Impulsor', 'P009', 500, 2000, 1, NOW()),
('Filtro', 'P010', 500, 2000, 1, NOW()),
('Cuerpo', 'P011', 500, 2000, 1, NOW()),
('Asiento', 'P012', 500, 2000, 1, NOW()),
('Motor', 'P013', 500, 2000, 1, NOW()),
('Válvula', 'P014', 500, 2000, 1, NOW()),
('Pistón', 'P015', 500, 2000, 1, NOW()),
('Camisa', 'P016', 500, 2000, 1, NOW()),
('Núcleo', 'P017', 500, 2000, 1, NOW()),
('Broca', 'P018', 500, 2000, 1, NOW()),
('Mandril', 'P019', 500, 2000, 1, NOW()),
('Tornillo', 'P020', 500, 2000, 1, NOW());


-- Inserción de datos en la tabla DetalleComponente
INSERT INTO componente_pieza_detallecomponente (idcomponente_id, idpieza_id, cantidad, estado) VALUES
(1, 1, 10, 1),
(1, 2, 5, 1),
(2, 3, 15, 1),
(2, 4, 8, 1),
(3, 5, 12, 1),
(3, 6, 7, 1),
(4, 7, 20, 1),
(4, 8, 10, 1),
(5, 1, 5, 1),
(5, 2, 3, 1),
(6, 3, 8, 1),
(6, 4, 6, 1),
(7, 5, 14, 1),
(7, 6, 9, 1),
(8, 7, 22, 1),
(8, 8, 11, 1);

-- CONFIGURACION
INSERT INTO componente_pieza_configuraciontipoimplemento (nombre_configuracion, estado)
VALUES
('CONFI CHASKI VIÑATERO', 1),
('CONFI AZUFRADORA', 1),
('CONFI JACTO', 1),
('CONFI ARADO', 1),
('CONFI ROTATIVA', 1);

-- DETALLE CONF
INSERT INTO componente_pieza_detalleconfiguracion (idcomponente_id, idconfiguracion_id, estado)
VALUES
(1, 1, 1),
(2, 1, 1),
(3, 2, 1),
(4, 2, 1),
(5, 3, 1),
(6, 3, 1),
(7, 4, 1),
(8, 4, 1),
(9, 5, 1),
(10, 5, 1),
(1, 2, 1),
(2, 2, 1),
(3, 3, 1),
(4, 3, 1),
(5, 4, 1),
(6, 4, 1),
(7, 5, 1),
(8, 5, 1),
(9, 1, 1),
(10, 1, 1),
(1, 3, 1),
(2, 3, 1),
(3, 4, 1),
(4, 4, 1),
(5, 5, 1),
(6, 5, 1),
(7, 1, 1),
(8, 1, 1),
(9, 2, 1),
(10, 2, 1);

#Tipo de implemento
select * from implemento_tipoimplemento;
INSERT INTO implemento_tipoimplemento (tipoimplemento, estado, tiempo_vida, frecuencia_man, idconfiguracion_implemento_id)
VALUES
('CHASKI', 1, 2000, 200, 1),
('AZUFRADORA', 1, 1000, 100, 2),
('JACTO', 1, 3000, 300, 3),
('ARADO', 1, 4000, 400, 4),
('ROTATIVA', 1, 5000, 500, 5);

INSERT INTO implemento_implemento(implemento,horasdeuso,codimplemento,estado,estado_actividad,idceco_id,idtipoimplemento_id,idusuario_id,mantenimientos,proximo_mantenimiento)
values
('ARADO1',0,'AR-0001'       ,1,1,1,1,2,0,400),
('ARADO2',0,'AR-0002'       ,1,1,1,1,3,0,400),
('AZUFRADORA1',0,'AZ-0001'  ,1,1,1,2,2,0,100),
('AZUFRADORA2',0,'AZ-0002'  ,1,1,1,2,3,0,100),
('CHASKI1',0,'CH-0001'      ,1,1,1,3,2,0,200),
('CHASKI2',0,'CH-0002'      ,1,1,1,3,3,0,200),
('JACTO1',0,'JA-0001'       ,1,1,1,4,2,0,300),
('JACTO2',0,'JA-0002'       ,1,1,1,4,3,0,300),
('ROTATIVA1',0,'RO-0001'    ,1,1,1,5,2,0,500),
('ROTATIVA2',0,'RO-0002'    ,1,1,1,5,3,0,500);

#tipo de tractores
INSERT INTO tractor_tipotractor (TipoTractor, estado) 
VALUES ('VIÑATERO', 1), 
       ('DOBLE', 1), 
       ('RETEN', 1), 
       ('SIMPLE', 1);
       
# tarctores
INSERT INTO tractor_tractor (nrotractor, horainicial,horauso,estado,estado_actividad,idfundo_id,idtipotractor_id,idusuario_id) 
VALUES 
('VIÑATERO1', 100,0,1,1,1,1,1), 
('VIÑATERO2', 100,0,1,1,1,1,2), 
('DOBLE1', 100,0,1,1,2,2,1), 
('DOBLE2', 100,0,1,1,2,2,2),  
('RETEN1', 100,0,1,1,3,3,1),  
('RETE2', 100,0,1,1,3,3,2),
('SIMPLE1', 100,0,1,1,4,4,1),
('SIMPLE2', 100,0,1,1,4,4,2);      
       
INSERT INTO programacion_labor_tipolabor (tipolabor, estado) 
VALUES 
('DESBROCE', 1), 
('APLICACIÓN', 1), 
('CIERRE DE CAMPO', 1), 
('MANT CAMINO', 1), 
('COSECHA', 1), 
('MANT DE CAMPO', 1), 
('PREPARACION', 1), 
('FUMIGACION', 1); 










		