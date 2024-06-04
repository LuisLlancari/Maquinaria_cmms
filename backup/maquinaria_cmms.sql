-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-06-2024 a las 00:47:17
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `maquinaria_cmms`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Persona', 6, 'add_persona'),
(22, 'Can change Persona', 6, 'change_persona'),
(23, 'Can delete Persona', 6, 'delete_persona'),
(24, 'Can view Persona', 6, 'view_persona'),
(25, 'Can add Rol', 7, 'add_rol'),
(26, 'Can change Rol', 7, 'change_rol'),
(27, 'Can delete Rol', 7, 'delete_rol'),
(28, 'Can view Rol', 7, 'view_rol'),
(29, 'Can add Usuario', 8, 'add_usuario'),
(30, 'Can change Usuario', 8, 'change_usuario'),
(31, 'Can delete Usuario', 8, 'delete_usuario'),
(32, 'Can view Usuario', 8, 'view_usuario'),
(33, 'Can add Reporte Tractor', 9, 'add_reportetractor'),
(34, 'Can change Reporte Tractor', 9, 'change_reportetractor'),
(35, 'Can delete Reporte Tractor', 9, 'delete_reportetractor'),
(36, 'Can view Reporte Tractor', 9, 'view_reportetractor'),
(37, 'Can add tipo tractor', 10, 'add_tipotractor'),
(38, 'Can change tipo tractor', 10, 'change_tipotractor'),
(39, 'Can delete tipo tractor', 10, 'delete_tipotractor'),
(40, 'Can view tipo tractor', 10, 'view_tipotractor'),
(41, 'Can add Tractor', 11, 'add_tractor'),
(42, 'Can change Tractor', 11, 'change_tractor'),
(43, 'Can delete Tractor', 11, 'delete_tractor'),
(44, 'Can view Tractor', 11, 'view_tractor'),
(45, 'Can add Sede', 12, 'add_sede'),
(46, 'Can change Sede', 12, 'change_sede'),
(47, 'Can delete Sede', 12, 'delete_sede'),
(48, 'Can view Sede', 12, 'view_sede'),
(49, 'Can add Base', 13, 'add_base'),
(50, 'Can change Base', 13, 'change_base'),
(51, 'Can delete Base', 13, 'delete_base'),
(52, 'Can view Base', 13, 'view_base'),
(53, 'Can add Area', 14, 'add_area'),
(54, 'Can change Area', 14, 'change_area'),
(55, 'Can delete Area', 14, 'delete_area'),
(56, 'Can view Area', 14, 'view_area'),
(57, 'Can add Cultivo', 15, 'add_cultivo'),
(58, 'Can change Cultivo', 15, 'change_cultivo'),
(59, 'Can delete Cultivo', 15, 'delete_cultivo'),
(60, 'Can view Cultivo', 15, 'view_cultivo'),
(61, 'Can add Fundo', 16, 'add_fundo'),
(62, 'Can change Fundo', 16, 'change_fundo'),
(63, 'Can delete Fundo', 16, 'delete_fundo'),
(64, 'Can view Fundo', 16, 'view_fundo'),
(65, 'Can add Variedad', 17, 'add_variedad'),
(66, 'Can change Variedad', 17, 'change_variedad'),
(67, 'Can delete Variedad', 17, 'delete_variedad'),
(68, 'Can view Variedad', 17, 'view_variedad'),
(69, 'Can add Lote', 18, 'add_lote'),
(70, 'Can change Lote', 18, 'change_lote'),
(71, 'Can delete Lote', 18, 'delete_lote'),
(72, 'Can view Lote', 18, 'view_lote'),
(73, 'Can add Detalle Implemento', 19, 'add_detimplementos'),
(74, 'Can change Detalle Implemento', 19, 'change_detimplementos'),
(75, 'Can delete Detalle Implemento', 19, 'delete_detimplementos'),
(76, 'Can view Detalle Implemento', 19, 'view_detimplementos'),
(77, 'Can add Tipo Implemento', 20, 'add_tipoimplemento'),
(78, 'Can change Tipo Implemento', 20, 'change_tipoimplemento'),
(79, 'Can delete Tipo Implemento', 20, 'delete_tipoimplemento'),
(80, 'Can view Tipo Implemento', 20, 'view_tipoimplemento'),
(81, 'Can add Implemento', 21, 'add_implemento'),
(82, 'Can change Implemento', 21, 'change_implemento'),
(83, 'Can delete Implemento', 21, 'delete_implemento'),
(84, 'Can view Implemento', 21, 'view_implemento'),
(85, 'Can add Componente', 22, 'add_componente'),
(86, 'Can change Componente', 22, 'change_componente'),
(87, 'Can delete Componente', 22, 'delete_componente'),
(88, 'Can view Componente', 22, 'view_componente'),
(89, 'Can add Configuracion Tipo Implemento', 23, 'add_configuraciontipoimplemento'),
(90, 'Can change Configuracion Tipo Implemento', 23, 'change_configuraciontipoimplemento'),
(91, 'Can delete Configuracion Tipo Implemento', 23, 'delete_configuraciontipoimplemento'),
(92, 'Can view Configuracion Tipo Implemento', 23, 'view_configuraciontipoimplemento'),
(93, 'Can add Pieza', 24, 'add_pieza'),
(94, 'Can change Pieza', 24, 'change_pieza'),
(95, 'Can delete Pieza', 24, 'delete_pieza'),
(96, 'Can view Pieza', 24, 'view_pieza'),
(97, 'Can add Sistema', 25, 'add_sistema'),
(98, 'Can change Sistema', 25, 'change_sistema'),
(99, 'Can delete Sistema', 25, 'delete_sistema'),
(100, 'Can view Sistema', 25, 'view_sistema'),
(101, 'Can add Detalles de Configuracion', 26, 'add_detalleconfiguracion'),
(102, 'Can change Detalles de Configuracion', 26, 'change_detalleconfiguracion'),
(103, 'Can delete Detalles de Configuracion', 26, 'delete_detalleconfiguracion'),
(104, 'Can view Detalles de Configuracion', 26, 'view_detalleconfiguracion'),
(105, 'Can add Detalles Componente', 27, 'add_detallecomponente'),
(106, 'Can change Detalles Componente', 27, 'change_detallecomponente'),
(107, 'Can delete Detalles Componente', 27, 'delete_detallecomponente'),
(108, 'Can view Detalles Componente', 27, 'view_detallecomponente'),
(109, 'Can add Solicitante', 28, 'add_solicitante'),
(110, 'Can change Solicitante', 28, 'change_solicitante'),
(111, 'Can delete Solicitante', 28, 'delete_solicitante'),
(112, 'Can view Solicitante', 28, 'view_solicitante'),
(113, 'Can add Tipo Solicitante', 29, 'add_tiposolicitante'),
(114, 'Can change Tipo Solicitante', 29, 'change_tiposolicitante'),
(115, 'Can delete Tipo Solicitante', 29, 'delete_tiposolicitante'),
(116, 'Can view Tipo Solicitante', 29, 'view_tiposolicitante'),
(117, 'Can add Tractorista', 30, 'add_tractorista'),
(118, 'Can change Tractorista', 30, 'change_tractorista'),
(119, 'Can delete Tractorista', 30, 'delete_tractorista'),
(120, 'Can view Tractorista', 30, 'view_tractorista'),
(121, 'Can add encargado', 31, 'add_encargado'),
(122, 'Can change encargado', 31, 'change_encargado'),
(123, 'Can delete encargado', 31, 'delete_encargado'),
(124, 'Can view encargado', 31, 'view_encargado'),
(125, 'Can add Detalle Labor', 32, 'add_detallelabor'),
(126, 'Can change Detalle Labor', 32, 'change_detallelabor'),
(127, 'Can delete Detalle Labor', 32, 'delete_detallelabor'),
(128, 'Can view Detalle Labor', 32, 'view_detallelabor'),
(129, 'Can add Tipo de labor', 33, 'add_tipolabor'),
(130, 'Can change Tipo de labor', 33, 'change_tipolabor'),
(131, 'Can delete Tipo de labor', 33, 'delete_tipolabor'),
(132, 'Can view Tipo de labor', 33, 'view_tipolabor'),
(133, 'Can add Programacion', 34, 'add_programacion'),
(134, 'Can change Programacion', 34, 'change_programacion'),
(135, 'Can delete Programacion', 34, 'delete_programacion'),
(136, 'Can view Programacion', 34, 'view_programacion'),
(137, 'Can add Ceco', 35, 'add_ceco'),
(138, 'Can change Ceco', 35, 'change_ceco'),
(139, 'Can delete Ceco', 35, 'delete_ceco'),
(140, 'Can view Ceco', 35, 'view_ceco'),
(141, 'Can add Acción', 36, 'add_acciones'),
(142, 'Can change Acción', 36, 'change_acciones'),
(143, 'Can delete Acción', 36, 'delete_acciones'),
(144, 'Can view Acción', 36, 'view_acciones'),
(145, 'Can add Detalle Cambio', 37, 'add_detallecambios'),
(146, 'Can change Detalle Cambio', 37, 'change_detallecambios'),
(147, 'Can delete Detalle Cambio', 37, 'delete_detallecambios'),
(148, 'Can view Detalle Cambio', 37, 'view_detallecambios'),
(149, 'Can add Detalle Mantenimiento', 38, 'add_detallemantenimiento'),
(150, 'Can change Detalle Mantenimiento', 38, 'change_detallemantenimiento'),
(151, 'Can delete Detalle Mantenimiento', 38, 'delete_detallemantenimiento'),
(152, 'Can view Detalle Mantenimiento', 38, 'view_detallemantenimiento'),
(153, 'Can add Motivo', 39, 'add_detmotivos'),
(154, 'Can change Motivo', 39, 'change_detmotivos'),
(155, 'Can delete Motivo', 39, 'delete_detmotivos'),
(156, 'Can view Motivo', 39, 'view_detmotivos'),
(157, 'Can add Diagnostico', 40, 'add_diagnostico'),
(158, 'Can change Diagnostico', 40, 'change_diagnostico'),
(159, 'Can delete Diagnostico', 40, 'delete_diagnostico'),
(160, 'Can view Diagnostico', 40, 'view_diagnostico'),
(161, 'Can add Programacion Mantenimiento', 41, 'add_programacionmantenimiento'),
(162, 'Can change Programacion Mantenimiento', 41, 'change_programacionmantenimiento'),
(163, 'Can delete Programacion Mantenimiento', 41, 'delete_programacionmantenimiento'),
(164, 'Can view Programacion Mantenimiento', 41, 'view_programacionmantenimiento'),
(165, 'Can add Mantenimiento', 42, 'add_mantenimiento'),
(166, 'Can change Mantenimiento', 42, 'change_mantenimiento'),
(167, 'Can delete Mantenimiento', 42, 'delete_mantenimiento'),
(168, 'Can view Mantenimiento', 42, 'view_mantenimiento'),
(169, 'Can add Recambio', 43, 'add_recambios'),
(170, 'Can change Recambio', 43, 'change_recambios'),
(171, 'Can delete Recambio', 43, 'delete_recambios'),
(172, 'Can view Recambio', 43, 'view_recambios');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ceco_ceco`
--

CREATE TABLE `ceco_ceco` (
  `idceco` int(11) NOT NULL,
  `ceco` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ceco_ceco`
--

INSERT INTO `ceco_ceco` (`idceco`, `ceco`, `estado`) VALUES
(1, 'CECO-001', 1),
(2, 'CECO-002', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_componente`
--

CREATE TABLE `componente_pieza_componente` (
  `idcomponente` int(11) NOT NULL,
  `componente` varchar(45) NOT NULL,
  `codcomponente` varchar(12) NOT NULL,
  `tiempovida` int(11) NOT NULL,
  `frecuencia_man` int(11) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL,
  `idsistema_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `componente_pieza_componente`
--

INSERT INTO `componente_pieza_componente` (`idcomponente`, `componente`, `codcomponente`, `tiempovida`, `frecuencia_man`, `estado`, `creado_en`, `actualizado_en`, `idsistema_id`) VALUES
(1, 'Motor Eléctrico', 'C001', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 1),
(2, 'Generador', 'C002', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 1),
(3, 'Torno', 'C003', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 2),
(4, 'Fresadora', 'C004', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 2),
(5, 'Bomba Hidráulica', 'C005', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 3),
(6, 'Válvula', 'C006', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 3),
(7, 'Compresor', 'C007', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 4),
(8, 'Cilindro Neumático', 'C008', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 4),
(9, 'Transformador', 'C009', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 1),
(10, 'Taladro', 'C010', 2000, 500, 1, '2024-06-04 14:21:53.000000', '2024-06-04', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_configuraciontipoimplemento`
--

CREATE TABLE `componente_pieza_configuraciontipoimplemento` (
  `idconfiguraciontipoimplemento` int(11) NOT NULL,
  `nombre_configuracion` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `componente_pieza_configuraciontipoimplemento`
--

INSERT INTO `componente_pieza_configuraciontipoimplemento` (`idconfiguraciontipoimplemento`, `nombre_configuracion`, `estado`) VALUES
(1, 'CONFI CHASKI VIÑATERO', 1),
(2, 'CONFI AZUFRADORA', 1),
(3, 'CONFI JACTO', 1),
(4, 'CONFI ARADO', 1),
(5, 'CONFI ROTATIVA', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_detallecomponente`
--

CREATE TABLE `componente_pieza_detallecomponente` (
  `iddetallecomponente` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idcomponente_id` int(11) NOT NULL,
  `idpieza_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `componente_pieza_detallecomponente`
--

INSERT INTO `componente_pieza_detallecomponente` (`iddetallecomponente`, `cantidad`, `estado`, `idcomponente_id`, `idpieza_id`) VALUES
(1, 10, 1, 1, 1),
(2, 5, 1, 1, 2),
(3, 15, 1, 2, 3),
(4, 8, 1, 2, 4),
(5, 12, 1, 3, 5),
(6, 7, 1, 3, 6),
(7, 20, 1, 4, 7),
(8, 10, 1, 4, 8),
(9, 5, 1, 5, 1),
(10, 3, 1, 5, 2),
(11, 8, 1, 6, 3),
(12, 6, 1, 6, 4),
(13, 14, 1, 7, 5),
(14, 9, 1, 7, 6),
(15, 22, 1, 8, 7),
(16, 11, 1, 8, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_detalleconfiguracion`
--

CREATE TABLE `componente_pieza_detalleconfiguracion` (
  `iddetallecomponente` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idcomponente_id` int(11) NOT NULL,
  `idconfiguracion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `componente_pieza_detalleconfiguracion`
--

INSERT INTO `componente_pieza_detalleconfiguracion` (`iddetallecomponente`, `estado`, `idcomponente_id`, `idconfiguracion_id`) VALUES
(1, 1, 1, 1),
(2, 1, 2, 1),
(3, 1, 3, 2),
(4, 1, 4, 2),
(5, 1, 5, 3),
(6, 1, 6, 3),
(7, 1, 7, 4),
(8, 1, 8, 4),
(9, 1, 9, 5),
(10, 1, 10, 5),
(11, 1, 1, 2),
(12, 1, 2, 2),
(13, 1, 3, 3),
(14, 1, 4, 3),
(15, 1, 5, 4),
(16, 1, 6, 4),
(17, 1, 7, 5),
(18, 1, 8, 5),
(19, 1, 9, 1),
(20, 1, 10, 1),
(21, 1, 1, 3),
(22, 1, 2, 3),
(23, 1, 3, 4),
(24, 1, 4, 4),
(25, 1, 5, 5),
(26, 1, 6, 5),
(27, 1, 7, 1),
(28, 1, 8, 1),
(29, 1, 9, 2),
(30, 1, 10, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_pieza`
--

CREATE TABLE `componente_pieza_pieza` (
  `idpieza` int(11) NOT NULL,
  `pieza` varchar(45) NOT NULL,
  `codpieza` varchar(12) NOT NULL,
  `frecuencia_man` int(11) NOT NULL,
  `tiempovida` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `componente_pieza_pieza`
--

INSERT INTO `componente_pieza_pieza` (`idpieza`, `pieza`, `codpieza`, `frecuencia_man`, `tiempovida`, `estado`, `creado_en`, `actualizado_en`) VALUES
(1, 'Bobina', 'P001', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(2, 'Rotor', 'P002', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(3, 'Estator', 'P003', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(4, 'Carcasa', 'P004', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(5, 'Cuchilla', 'P005', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(6, 'Mandril', 'P006', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(7, 'Mesa', 'P007', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(8, 'Cabezal', 'P008', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(9, 'Impulsor', 'P009', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(10, 'Filtro', 'P010', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(11, 'Cuerpo', 'P011', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(12, 'Asiento', 'P012', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(13, 'Motor', 'P013', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(14, 'Válvula', 'P014', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(15, 'Pistón', 'P015', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(16, 'Camisa', 'P016', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(17, 'Núcleo', 'P017', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(18, 'Broca', 'P018', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(19, 'Mandril', 'P019', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04'),
(20, 'Tornillo', 'P020', 500, 2000, 1, '2024-06-04 14:21:57.000000', '2024-06-04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_sistema`
--

CREATE TABLE `componente_pieza_sistema` (
  `idsistema` int(11) NOT NULL,
  `sistema` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `componente_pieza_sistema`
--

INSERT INTO `componente_pieza_sistema` (`idsistema`, `sistema`, `estado`) VALUES
(1, 'Eléctrico', 1),
(2, 'Mecánico', 1),
(3, 'Hidráulico', 1),
(4, 'Neumático', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-06-04 19:16:16.239467', '1', '  1', 2, '[{\"changed\": {\"fields\": [\"Rol\"]}}]', 8, 1),
(2, '2024-06-04 19:34:07.295261', '5', 'Mecanico', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-06-04 20:00:03.521967', '1', 'Mantenimiento General', 1, '[{\"added\": {}}]', 36, 1),
(4, '2024-06-04 20:00:19.693289', '2', 'Fuga de Aceite', 1, '[{\"added\": {}}]', 36, 1),
(5, '2024-06-04 20:01:41.121571', '1', '1222', 1, '[{\"added\": {}}]', 18, 1),
(6, '2024-06-04 20:01:49.567959', '2', '1223', 1, '[{\"added\": {}}]', 18, 1),
(7, '2024-06-04 20:01:57.768060', '3', '1224', 1, '[{\"added\": {}}]', 18, 1),
(8, '2024-06-04 20:02:08.549940', '4', '2221', 1, '[{\"added\": {}}]', 18, 1),
(9, '2024-06-04 20:56:37.718720', '2', 'AZUFRADORA', 2, '[]', 20, 1),
(10, '2024-06-04 20:56:43.169411', '2', 'AZUFRADORA 1', 2, '[{\"changed\": {\"fields\": [\"Horas de uso\"]}}]', 21, 1),
(11, '2024-06-04 20:59:46.184281', '3', 'falla electrica', 1, '[{\"added\": {}}]', 36, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(35, 'ceco', 'ceco'),
(22, 'componente_pieza', 'componente'),
(23, 'componente_pieza', 'configuraciontipoimplemento'),
(27, 'componente_pieza', 'detallecomponente'),
(26, 'componente_pieza', 'detalleconfiguracion'),
(24, 'componente_pieza', 'pieza'),
(25, 'componente_pieza', 'sistema'),
(4, 'contenttypes', 'contenttype'),
(15, 'fundo_cultivo', 'cultivo'),
(16, 'fundo_cultivo', 'fundo'),
(18, 'fundo_cultivo', 'lote'),
(17, 'fundo_cultivo', 'variedad'),
(19, 'implemento', 'detimplementos'),
(21, 'implemento', 'implemento'),
(20, 'implemento', 'tipoimplemento'),
(14, 'localizacion', 'area'),
(13, 'localizacion', 'base'),
(12, 'localizacion', 'sede'),
(36, 'mantenimiento', 'acciones'),
(37, 'mantenimiento', 'detallecambios'),
(38, 'mantenimiento', 'detallemantenimiento'),
(39, 'mantenimiento', 'detmotivos'),
(40, 'mantenimiento', 'diagnostico'),
(42, 'mantenimiento', 'mantenimiento'),
(41, 'mantenimiento', 'programacionmantenimiento'),
(43, 'mantenimiento', 'recambios'),
(31, 'operarios', 'encargado'),
(28, 'operarios', 'solicitante'),
(29, 'operarios', 'tiposolicitante'),
(30, 'operarios', 'tractorista'),
(32, 'programacion_labor', 'detallelabor'),
(34, 'programacion_labor', 'programacion'),
(33, 'programacion_labor', 'tipolabor'),
(5, 'sessions', 'session'),
(9, 'tractor', 'reportetractor'),
(10, 'tractor', 'tipotractor'),
(11, 'tractor', 'tractor'),
(6, 'usuario', 'persona'),
(7, 'usuario', 'rol'),
(8, 'usuario', 'usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-04 19:00:35.690948'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-06-04 19:00:35.754101'),
(3, 'auth', '0001_initial', '2024-06-04 19:00:35.865640'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-06-04 19:00:35.881296'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-06-04 19:00:35.896921'),
(6, 'auth', '0004_alter_user_username_opts', '2024-06-04 19:00:35.896921'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-06-04 19:00:35.896921'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-06-04 19:00:35.896921'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-06-04 19:00:35.896921'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-06-04 19:00:35.914320'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-06-04 19:00:35.914320'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-06-04 19:00:35.914320'),
(13, 'auth', '0011_update_proxy_permissions', '2024-06-04 19:00:35.914320'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-06-04 19:00:35.929984'),
(15, 'usuario', '0001_initial', '2024-06-04 19:00:38.012704'),
(16, 'admin', '0001_initial', '2024-06-04 19:00:38.090819'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-06-04 19:00:38.090819'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-04 19:00:38.139756'),
(19, 'ceco', '0001_initial', '2024-06-04 19:00:38.139756'),
(20, 'componente_pieza', '0001_initial', '2024-06-04 19:00:38.313998'),
(21, 'localizacion', '0001_initial', '2024-06-04 19:00:38.378458'),
(22, 'fundo_cultivo', '0001_initial', '2024-06-04 19:00:38.474201'),
(23, 'implemento', '0001_initial', '2024-06-04 19:00:38.554361'),
(24, 'implemento', '0002_initial', '2024-06-04 19:00:38.648404'),
(25, 'operarios', '0001_initial', '2024-06-04 19:00:38.666113'),
(26, 'operarios', '0002_initial', '2024-06-04 19:00:38.778338'),
(27, 'operarios', '0003_encargado', '2024-06-04 19:00:38.809596'),
(28, 'mantenimiento', '0001_initial', '2024-06-04 19:00:38.921044'),
(29, 'mantenimiento', '0002_initial', '2024-06-04 19:00:39.740473'),
(30, 'mantenimiento', '0003_recambios_remove_detallemantenimiento_completado_and_more', '2024-06-04 19:00:39.771752'),
(31, 'mantenimiento', '0004_remove_detallemantenimiento_realizado_and_more', '2024-06-04 19:00:39.773611'),
(32, 'mantenimiento', '0005_recambios_idmantenimiento', '2024-06-04 19:00:39.821140'),
(33, 'mantenimiento', '0006_alter_mantenimiento_persona', '2024-06-04 19:00:41.269450'),
(34, 'tractor', '0001_initial', '2024-06-04 19:00:41.350212'),
(35, 'programacion_labor', '0001_initial', '2024-06-04 19:00:41.461673'),
(36, 'programacion_labor', '0002_initial', '2024-06-04 19:00:41.539795'),
(37, 'programacion_labor', '0003_initial', '2024-06-04 19:00:41.669452'),
(38, 'sessions', '0001_initial', '2024-06-04 19:00:41.685117'),
(39, 'tractor', '0002_initial', '2024-06-04 19:00:41.875119'),
(40, 'operarios', '0004_rename_persona_encargado_idpersona', '2024-06-04 21:52:02.762243'),
(41, 'mantenimiento', '0007_remove_mantenimiento_persona_and_more', '2024-06-04 21:52:03.533865');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7nuo5h9y9xkv8b07med7bxt18tdacixa', '.eJxVjEEOwiAQRe_C2hAojFCX7nsGMgMzUjVtUtqV8e7apAvd_vfef6mE21rT1nhJY1EXBer0uxHmB087KHecbrPO87QuI-ld0QdtepgLP6-H-3dQsdVv7XuKzgCSBBIGDhSi4VJsD84F6MQRI3cWBMR3kdFKLz6HGEOJhs7q_QH44DhR:1sEaRp:Hw-Les-y3Cj3rFCEHv8FnewHgky6lj7CU0BlNTDAMQw', '2024-06-18 20:07:57.965681'),
('af9g4duuaj7krp1sac6c82l14tbxlxaz', '.eJxVjMsOwiAQRf-FtSEEpjxcuvcbyMAwUjWQlHZl_Hdt0oVu7znnvkTEba1xG2WJM4mzAHH63RLmR2k7oDu2W5e5t3WZk9wVedAhr53K83K4fwcVR_3WfkJkUhaSSx600Zis4WBUZjTBMXiA4C1j0jCxccAqhwyelAtkmMX7A-QwN-0:1sEZvg:C4Fwy1jzjllzE-qdsSo_jLXg5oom_MT_E1fzyZ_4TL0', '2024-06-18 19:34:44.621201'),
('ctkqo4lm1z4cish7fxutzp1jfy65412c', '.eJxVjEEOwiAURO_C2hD6W1Jw6d4zEIb_kaqhSWlXxrtrky50O--9eakQt7WErckSJlZn1anT74aYHlJ3wPdYb7NOc12XCXpX9EGbvs4sz8vh_h2U2Mq39p6s70gMgzkjke0t0WjBzmUaBmRkEQi87SEOBDEYMxsgRTGi3h8CGDmo:1sEceR:F7Fc9a86qXYUNf5kNd4omWvJ3ybldjX8ho9lVS9vEMw', '2024-06-18 22:29:07.993373'),
('e4amj611ns9c23u2pag7o0lou16qldhu', '.eJxVjDsOwjAQRO_iGln-ZP2hpOcM1u7a4ABypDipEHcnkVJANdK8N_MWCdelprWXOY1ZnIUXp9-OkJ-l7SA_sN0nyVNb5pHkrsiDdnmdcnldDvfvoGKv2xrZeKNYBwCwRvuIxeJNKYdag8ochxiYwBIFBBsNocPBO5e3iMZ68fkCxzA3CA:1sEbwn:VExHlQft-gRmH2y-7P9sWDatVmEYZ5ElA0Vqp_TiRiE', '2024-06-18 21:44:01.573440'),
('s9pa76ppbyhngifogr6zqfirjtyqhopc', '.eJxVjM0OwiAQhN-FsyHL8iN69N5nIMAuUjU0Ke3J-O62SQ96nPm-mbcIcV1qWDvPYSRxFU6cfrsU85PbDugR232SeWrLPCa5K_KgXQ4T8et2uH8HNfa6rT2TZgQGz85bBHI2JSoZFBOBcV4RnFXRW0rGYtGQ0SilL9poaxDF5wvt2zdb:1sEadc:gvxGUtgD0zkbx1p3GileiTXHImG6RWCpgfxABT4bjno', '2024-06-18 20:20:08.030696');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_cultivo`
--

CREATE TABLE `fundo_cultivo_cultivo` (
  `idcultivo` int(11) NOT NULL,
  `cultivo` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fundo_cultivo_cultivo`
--

INSERT INTO `fundo_cultivo_cultivo` (`idcultivo`, `cultivo`, `estado`) VALUES
(1, 'Esparrago', 1),
(2, 'Arandanos', 1),
(3, 'Granada', 1),
(4, 'Pecano', 1),
(5, 'Palto', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_fundo`
--

CREATE TABLE `fundo_cultivo_fundo` (
  `idfundo` int(11) NOT NULL,
  `fundo` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idsede_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fundo_cultivo_fundo`
--

INSERT INTO `fundo_cultivo_fundo` (`idfundo`, `fundo`, `estado`, `idsede_id`) VALUES
(1, 'Fortuna', 1, NULL),
(2, 'San Isidro', 1, NULL),
(3, 'Luren', 1, NULL),
(4, 'Karla', 1, NULL),
(5, 'Gloria', 1, NULL),
(6, 'Dos Maria', 1, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_lote`
--

CREATE TABLE `fundo_cultivo_lote` (
  `idlote` int(11) NOT NULL,
  `lote` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idfundo_id` int(11) DEFAULT NULL,
  `idvariedad_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fundo_cultivo_lote`
--

INSERT INTO `fundo_cultivo_lote` (`idlote`, `lote`, `estado`, `idfundo_id`, `idvariedad_id`) VALUES
(1, '1222', 1, 1, 1),
(2, '1223', 1, 1, 2),
(3, '1224', 1, 1, 3),
(4, '2221', 1, 2, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_variedad`
--

CREATE TABLE `fundo_cultivo_variedad` (
  `idvariedad` int(11) NOT NULL,
  `variedad` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idcultivo_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fundo_cultivo_variedad`
--

INSERT INTO `fundo_cultivo_variedad` (`idvariedad`, `variedad`, `estado`, `idcultivo_id`) VALUES
(1, 'Espárragos trigueros', 1, 1),
(2, 'Espárragos gruesos', 1, 1),
(3, 'Espárragos delgados', 1, 1),
(4, 'Fuerte', 1, 5),
(5, 'Hass', 1, 5),
(6, 'Pinkerton', 1, 5),
(7, 'Biloxi', 1, 2),
(8, 'Ventura', 1, 2),
(9, 'Jewel', 1, 2),
(10, 'Wonderful', 1, 3),
(11, 'Western Schley', 1, 4),
(12, 'Wichita', 1, 4),
(13, 'Mahan', 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `implemento_detimplementos`
--

CREATE TABLE `implemento_detimplementos` (
  `iddetalleimplemento` int(11) NOT NULL,
  `MRimplemento` int(11) NOT NULL,
  `MRcomponente` int(11) NOT NULL,
  `HUcomponente` decimal(10,2) NOT NULL,
  `CRcomponente` int(11) NOT NULL,
  `cantidadpieza` int(11) NOT NULL,
  `MRpieza` int(11) NOT NULL,
  `HUpieza` decimal(10,2) NOT NULL,
  `CRpieza` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `iddetallecomponente_id` int(11) NOT NULL,
  `idimplemento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `implemento_detimplementos`
--

INSERT INTO `implemento_detimplementos` (`iddetalleimplemento`, `MRimplemento`, `MRcomponente`, `HUcomponente`, `CRcomponente`, `cantidadpieza`, `MRpieza`, `HUpieza`, `CRpieza`, `estado`, `iddetallecomponente_id`, `idimplemento_id`) VALUES
(1, 0, 0, 0.00, 0, 14, 0, 0.00, 0, 1, 13, 1),
(2, 0, 0, 0.00, 0, 9, 0, 0.00, 0, 1, 14, 1),
(3, 0, 0, 0.00, 0, 22, 0, 0.00, 0, 1, 15, 1),
(4, 0, 0, 0.00, 0, 11, 0, 0.00, 0, 1, 16, 1),
(5, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 9, 1),
(6, 0, 0, 0.00, 0, 3, 0, 0.00, 0, 1, 10, 1),
(7, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 11, 1),
(8, 0, 0, 0.00, 0, 6, 0, 0.00, 0, 1, 12, 1),
(9, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 1),
(10, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 1),
(11, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 1),
(12, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 1),
(13, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 2),
(14, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 2),
(15, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 2),
(16, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 2),
(17, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 2),
(18, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 2),
(19, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 2),
(20, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 2),
(21, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 3),
(22, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 3),
(23, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 3),
(24, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 3),
(25, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 3),
(26, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 3),
(27, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 3),
(28, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 3),
(29, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 4),
(30, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 4),
(31, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 4),
(32, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 4),
(33, 0, 0, 0.00, 0, 14, 0, 0.00, 0, 1, 13, 4),
(34, 0, 0, 0.00, 0, 9, 0, 0.00, 0, 1, 14, 4),
(35, 0, 0, 0.00, 0, 22, 0, 0.00, 0, 1, 15, 4),
(36, 0, 0, 0.00, 0, 11, 0, 0.00, 0, 1, 16, 4),
(37, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 5),
(38, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 5),
(39, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 5),
(40, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 5),
(41, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 5),
(42, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 5),
(43, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 5),
(44, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 5),
(45, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 6),
(46, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 6),
(47, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 6),
(48, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 6),
(49, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 6),
(50, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 6),
(51, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 6),
(52, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 6),
(53, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 9, 7),
(54, 0, 0, 0.00, 0, 3, 0, 0.00, 0, 1, 10, 7),
(55, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 11, 7),
(56, 0, 0, 0.00, 0, 6, 0, 0.00, 0, 1, 12, 7),
(57, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 7),
(58, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 7),
(59, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 7),
(60, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 7),
(61, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 7),
(62, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 7),
(63, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 7),
(64, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 7),
(65, 0, 0, 0.00, 0, 14, 0, 0.00, 0, 1, 13, 8),
(66, 0, 0, 0.00, 0, 9, 0, 0.00, 0, 1, 14, 8),
(67, 0, 0, 0.00, 0, 22, 0, 0.00, 0, 1, 15, 8),
(68, 0, 0, 0.00, 0, 11, 0, 0.00, 0, 1, 16, 8),
(69, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 9, 8),
(70, 0, 0, 0.00, 0, 3, 0, 0.00, 0, 1, 10, 8),
(71, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 11, 8),
(72, 0, 0, 0.00, 0, 6, 0, 0.00, 0, 1, 12, 8),
(73, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 9, 9),
(74, 0, 0, 0.00, 0, 3, 0, 0.00, 0, 1, 10, 9),
(75, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 11, 9),
(76, 0, 0, 0.00, 0, 6, 0, 0.00, 0, 1, 12, 9),
(77, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 9),
(78, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 9),
(79, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 9),
(80, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 9),
(81, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 1, 9),
(82, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 2, 9),
(83, 0, 0, 0.00, 0, 15, 0, 0.00, 0, 1, 3, 9),
(84, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 4, 9),
(85, 0, 0, 0.00, 0, 14, 0, 0.00, 0, 1, 13, 10),
(86, 0, 0, 0.00, 0, 9, 0, 0.00, 0, 1, 14, 10),
(87, 0, 0, 0.00, 0, 22, 0, 0.00, 0, 1, 15, 10),
(88, 0, 0, 0.00, 0, 11, 0, 0.00, 0, 1, 16, 10),
(89, 0, 0, 0.00, 0, 5, 0, 0.00, 0, 1, 9, 10),
(90, 0, 0, 0.00, 0, 3, 0, 0.00, 0, 1, 10, 10),
(91, 0, 0, 0.00, 0, 8, 0, 0.00, 0, 1, 11, 10),
(92, 0, 0, 0.00, 0, 6, 0, 0.00, 0, 1, 12, 10),
(93, 0, 0, 0.00, 0, 12, 0, 0.00, 0, 1, 5, 10),
(94, 0, 0, 0.00, 0, 7, 0, 0.00, 0, 1, 6, 10),
(95, 0, 0, 0.00, 0, 20, 0, 0.00, 0, 1, 7, 10),
(96, 0, 0, 0.00, 0, 10, 0, 0.00, 0, 1, 8, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `implemento_implemento`
--

CREATE TABLE `implemento_implemento` (
  `idimplemento` int(11) NOT NULL,
  `implemento` varchar(45) NOT NULL,
  `horasdeuso` double NOT NULL,
  `codimplemento` varchar(12) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `estado_actividad` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL,
  `idceco_id` int(11) NOT NULL,
  `idtipoimplemento_id` int(11) NOT NULL,
  `idusuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `implemento_implemento`
--

INSERT INTO `implemento_implemento` (`idimplemento`, `implemento`, `horasdeuso`, `codimplemento`, `estado`, `estado_actividad`, `creado_en`, `actualizado_en`, `idceco_id`, `idtipoimplemento_id`, `idusuario_id`) VALUES
(1, 'ARADO 1', 21.6, 'AR-00001', 1, 1, '2024-06-04 20:04:38.174992', '2024-06-04', 1, 4, 2),
(2, 'AZUFRADORA 1', 56, 'AZ-0001', 1, 1, '2024-06-04 20:32:47.585317', '2024-06-04', 1, 2, 1),
(3, 'AZUFRADORA 2', 0, 'AZ-0002', 1, 1, '2024-06-04 20:33:19.257392', '2024-06-04', 1, 2, 1),
(4, 'CHASKI1', 0, 'CH-10001', 1, 1, '2024-06-04 20:33:53.563134', '2024-06-04', 1, 1, 2),
(5, 'AZUFRADORA 3', 0, 'AZ-0003', 1, 1, '2024-06-04 20:34:10.841045', '2024-06-04', 1, 2, 1),
(6, 'AZUFRADORA', 9, 'AZ-10009', 1, 1, '2024-06-04 20:34:14.533450', '2024-06-04', 1, 2, 2),
(7, 'JACTO 1', 0, 'JA-0001', 1, 1, '2024-06-04 20:34:37.844899', '2024-06-04', 2, 3, 1),
(8, 'ROTATIVA', 9, 'RO-10001', 1, 1, '2024-06-04 20:34:38.632497', '2024-06-04', 1, 5, 2),
(9, 'JACTO 2', 0, 'JA-0002', 1, 1, '2024-06-04 20:35:10.174455', '2024-06-04', 2, 3, 1),
(10, 'ARADO2', 0, 'AR-10001', 1, 1, '2024-06-04 20:35:11.050280', '2024-06-04', 1, 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `implemento_tipoimplemento`
--

CREATE TABLE `implemento_tipoimplemento` (
  `idtipoimplemento` int(11) NOT NULL,
  `tipoimplemento` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `tiempo_vida` int(11) NOT NULL,
  `frecuencia_man` int(11) NOT NULL,
  `idconfiguracion_implemento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `implemento_tipoimplemento`
--

INSERT INTO `implemento_tipoimplemento` (`idtipoimplemento`, `tipoimplemento`, `estado`, `tiempo_vida`, `frecuencia_man`, `idconfiguracion_implemento_id`) VALUES
(1, 'CHASKI', 1, 2000, 200, 1),
(2, 'AZUFRADORA', 1, 1000, 100, 2),
(3, 'JACTO', 1, 3000, 300, 3),
(4, 'ARADO', 1, 4000, 400, 4),
(5, 'ROTATIVA', 1, 5000, 500, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizacion_area`
--

CREATE TABLE `localizacion_area` (
  `idarea` int(11) NOT NULL,
  `area` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idbase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizacion_base`
--

CREATE TABLE `localizacion_base` (
  `idbase` int(11) NOT NULL,
  `base` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idsede_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizacion_sede`
--

CREATE TABLE `localizacion_sede` (
  `idsede` int(11) NOT NULL,
  `sede` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `localizacion_sede`
--

INSERT INTO `localizacion_sede` (`idsede`, `sede`, `estado`) VALUES
(1, 'Chincha', 1),
(2, 'Ica', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_acciones`
--

CREATE TABLE `mantenimiento_acciones` (
  `idaccion` int(11) NOT NULL,
  `accion` varchar(45) NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mantenimiento_acciones`
--

INSERT INTO `mantenimiento_acciones` (`idaccion`, `accion`, `estado`) VALUES
(1, 'Mantenimiento General', 0),
(2, 'Fuga de Aceite', 0),
(3, 'falla electrica', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_detallecambios`
--

CREATE TABLE `mantenimiento_detallecambios` (
  `iddetallecambio` int(11) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `iddetalleimplemento_id` int(11) NOT NULL,
  `idmantenimiento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_detallemantenimiento`
--

CREATE TABLE `mantenimiento_detallemantenimiento` (
  `iddetallemantenimiento` int(11) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idaccion_id` int(11) NOT NULL,
  `idmantenimiento_id` int(11) NOT NULL,
  `completado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mantenimiento_detallemantenimiento`
--

INSERT INTO `mantenimiento_detallemantenimiento` (`iddetallemantenimiento`, `creado_en`, `estado`, `idaccion_id`, `idmantenimiento_id`, `completado`) VALUES
(1, '2024-06-04 22:18:07.993292', 1, 2, 1, 0),
(2, '2024-06-04 22:27:22.220208', 1, 1, 2, 1),
(3, '2024-06-04 22:27:22.224206', 1, 3, 2, 1),
(4, '2024-06-04 22:27:22.226207', 1, 3, 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_detmotivos`
--

CREATE TABLE `mantenimiento_detmotivos` (
  `iddetmotivo` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `idaccion_id` int(11) NOT NULL,
  `idprogramacionmantenimiento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mantenimiento_detmotivos`
--

INSERT INTO `mantenimiento_detmotivos` (`iddetmotivo`, `created_at`, `idaccion_id`, `idprogramacionmantenimiento_id`) VALUES
(1, '2024-06-04 21:11:27.837994', 2, 2),
(2, '2024-06-04 21:13:36.147423', 1, 1),
(3, '2024-06-04 21:13:36.149468', 2, 1),
(4, '2024-06-04 21:13:36.150958', 3, 1),
(5, '2024-06-04 22:29:40.812455', 2, 3),
(6, '2024-06-04 22:29:40.812455', 3, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_diagnostico`
--

CREATE TABLE `mantenimiento_diagnostico` (
  `iddiagnostico` int(11) NOT NULL,
  `diagnostico` varchar(45) NOT NULL,
  `det` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_mantenimiento`
--

CREATE TABLE `mantenimiento_mantenimiento` (
  `idmantenimiento` int(11) NOT NULL,
  `fechaingreso` date DEFAULT NULL,
  `fechasalida` date DEFAULT NULL,
  `descripcion` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idprogramacionmantenimiento_id` int(11) NOT NULL,
  `idencargado_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mantenimiento_mantenimiento`
--

INSERT INTO `mantenimiento_mantenimiento` (`idmantenimiento`, `fechaingreso`, `fechasalida`, `descripcion`, `estado`, `idprogramacionmantenimiento_id`, `idencargado_id`) VALUES
(1, '2024-06-04', '2024-06-06', '', 0, 2, 1),
(2, '2024-06-04', '2024-06-08', '', 0, 1, 1),
(3, NULL, NULL, '', 1, 3, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_programacionmantenimiento`
--

CREATE TABLE `mantenimiento_programacionmantenimiento` (
  `idprogramacionmantenimiento` int(11) NOT NULL,
  `fechaprogramacion` date DEFAULT NULL,
  `tipomantenimiento` int(11) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `idimplemento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mantenimiento_programacionmantenimiento`
--

INSERT INTO `mantenimiento_programacionmantenimiento` (`idprogramacionmantenimiento`, `fechaprogramacion`, `tipomantenimiento`, `estado`, `idimplemento_id`) VALUES
(1, '2024-06-07', 1, 1, 2),
(2, '2024-06-05', 0, 1, 2),
(3, '2024-06-10', 0, 1, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_recambios`
--

CREATE TABLE `mantenimiento_recambios` (
  `idrecambio` int(11) NOT NULL,
  `item` varchar(45) NOT NULL,
  `codigo` varchar(12) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `idmantenimiento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mantenimiento_recambios`
--

INSERT INTO `mantenimiento_recambios` (`idrecambio`, `item`, `codigo`, `estado`, `creado_en`, `idmantenimiento_id`) VALUES
(1, 'Cuchilla', 'P005', 1, '2024-06-04 22:18:08.014548', 1),
(2, 'Cabezal', 'P008', 1, '2024-06-04 22:18:08.015596', 1),
(3, 'Cuchilla', 'P005', 1, '2024-06-04 22:27:22.227233', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operarios_encargado`
--

CREATE TABLE `operarios_encargado` (
  `idencargado` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idpersona_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `operarios_encargado`
--

INSERT INTO `operarios_encargado` (`idencargado`, `estado`, `idpersona_id`) VALUES
(1, 1, 10),
(2, 1, 11),
(3, 1, 12),
(4, 1, 13),
(5, 1, 14),
(6, 1, 15),
(7, 1, 16),
(8, 1, 17);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operarios_solicitante`
--

CREATE TABLE `operarios_solicitante` (
  `idsolicitante` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `estado_actividad` tinyint(1) NOT NULL,
  `creado_en` datetime(6) DEFAULT NULL,
  `actualizado_en` date DEFAULT NULL,
  `idpersona_id` int(11) NOT NULL,
  `idtiposolicitante_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `operarios_solicitante`
--

INSERT INTO `operarios_solicitante` (`idsolicitante`, `estado`, `estado_actividad`, `creado_en`, `actualizado_en`, `idpersona_id`, `idtiposolicitante_id`) VALUES
(1, 1, 1, NULL, NULL, 6, 1),
(2, 1, 1, NULL, NULL, 7, 1),
(3, 1, 1, NULL, NULL, 8, 2),
(4, 1, 1, NULL, NULL, 9, 2),
(5, 1, 1, NULL, NULL, 10, 1),
(11, 1, 1, NULL, NULL, 16, 2),
(12, 1, 1, NULL, NULL, 17, 2),
(13, 1, 1, NULL, NULL, 18, 2),
(14, 1, 1, NULL, NULL, 19, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operarios_tiposolicitante`
--

CREATE TABLE `operarios_tiposolicitante` (
  `idtiposolicitante` int(11) NOT NULL,
  `tiposolicitante` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `operarios_tiposolicitante`
--

INSERT INTO `operarios_tiposolicitante` (`idtiposolicitante`, `tiposolicitante`, `estado`) VALUES
(1, 'Jefe Fundo', 1),
(2, 'Jefe de Sanidad', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operarios_tractorista`
--

CREATE TABLE `operarios_tractorista` (
  `idtractorista` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `estado_actividad` tinyint(1) NOT NULL,
  `creado_en` datetime(6) DEFAULT NULL,
  `actualizado_en` date NOT NULL,
  `idpersona_id` int(11) NOT NULL,
  `idusuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `operarios_tractorista`
--

INSERT INTO `operarios_tractorista` (`idtractorista`, `estado`, `estado_actividad`, `creado_en`, `actualizado_en`, `idpersona_id`, `idusuario_id`) VALUES
(1, 1, 1, NULL, '0000-00-00', 1, 1),
(2, 1, 1, NULL, '0000-00-00', 2, 1),
(3, 1, 1, NULL, '0000-00-00', 3, 1),
(4, 1, 1, NULL, '0000-00-00', 4, 1),
(5, 1, 1, NULL, '0000-00-00', 5, 1),
(6, 1, 1, NULL, '0000-00-00', 11, 2),
(7, 1, 1, NULL, '0000-00-00', 12, 2),
(8, 1, 1, NULL, '0000-00-00', 13, 2),
(9, 1, 1, NULL, '0000-00-00', 14, 2),
(10, 1, 1, NULL, '0000-00-00', 15, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programacion_labor_detallelabor`
--

CREATE TABLE `programacion_labor_detallelabor` (
  `iddetlabor` int(11) NOT NULL,
  `horadeuso` int(11) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `idimplemento_id` int(11) DEFAULT NULL,
  `idprogramacion_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `programacion_labor_detallelabor`
--

INSERT INTO `programacion_labor_detallelabor` (`iddetlabor`, `horadeuso`, `estado`, `idimplemento_id`, `idprogramacion_id`) VALUES
(1, 14, 1, 1, 1),
(2, 10, 1, 1, 2),
(3, 10, 1, 6, 3),
(4, 10, 1, 8, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programacion_labor_programacion`
--

CREATE TABLE `programacion_labor_programacion` (
  `idprogramacion` int(11) NOT NULL,
  `fechahora` date NOT NULL,
  `turno` varchar(1) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idlote_id` int(11) DEFAULT NULL,
  `idsolicitante_id` int(11) DEFAULT NULL,
  `idtipolabor_id` int(11) DEFAULT NULL,
  `idtractor_id` int(11) DEFAULT NULL,
  `idtractorista_id` int(11) DEFAULT NULL,
  `idusuario_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `programacion_labor_programacion`
--

INSERT INTO `programacion_labor_programacion` (`idprogramacion`, `fechahora`, `turno`, `estado`, `idlote_id`, `idsolicitante_id`, `idtipolabor_id`, `idtractor_id`, `idtractorista_id`, `idusuario_id`) VALUES
(1, '2024-06-04', 'M', 0, 1, 1, 1, 2, 1, 1),
(2, '2024-06-04', 'T', 0, 4, 2, 3, 7, 6, 1),
(3, '2024-06-04', 'M', 0, 1, 1, 4, 10, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programacion_labor_tipolabor`
--

CREATE TABLE `programacion_labor_tipolabor` (
  `idtipolabor` int(11) NOT NULL,
  `tipolabor` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `programacion_labor_tipolabor`
--

INSERT INTO `programacion_labor_tipolabor` (`idtipolabor`, `tipolabor`, `estado`) VALUES
(1, 'DESBROCE', 1),
(2, 'APLICACIÓN', 1),
(3, 'CIERRE DE CAMPO', 1),
(4, 'MANT CAMINO', 1),
(5, 'COSECHA', 1),
(6, 'MANT DE CAMPO', 1),
(7, 'PREPARACION', 1),
(8, 'FUMIGACION', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tractor_reportetractor`
--

CREATE TABLE `tractor_reportetractor` (
  `idreportetractor` int(11) NOT NULL,
  `horometroinicial` int(11) NOT NULL,
  `horometrofinal` int(11) NOT NULL,
  `correlativo` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idprogramacion_id` int(11) NOT NULL,
  `idusuario_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tractor_reportetractor`
--

INSERT INTO `tractor_reportetractor` (`idreportetractor`, `horometroinicial`, `horometrofinal`, `correlativo`, `estado`, `idprogramacion_id`, `idusuario_id`) VALUES
(1, 100, 110, 12341, 1, 2, 5),
(2, 100, 114, 12363, 1, 1, 5),
(3, 100, 110, 55551, 1, 3, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tractor_tipotractor`
--

CREATE TABLE `tractor_tipotractor` (
  `idtipotractor` int(11) NOT NULL,
  `TipoTractor` varchar(100) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tractor_tipotractor`
--

INSERT INTO `tractor_tipotractor` (`idtipotractor`, `TipoTractor`, `estado`) VALUES
(1, 'VIÑATERO', 1),
(2, 'DOBLE', 1),
(3, 'RETEN', 1),
(4, 'SIMPLE', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tractor_tractor`
--

CREATE TABLE `tractor_tractor` (
  `idtractor` int(11) NOT NULL,
  `nrotractor` varchar(100) NOT NULL,
  `horainicial` int(11) NOT NULL,
  `horauso` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `estado_actividad` tinyint(1) NOT NULL,
  `idfundo_id` int(11) DEFAULT NULL,
  `idtipotractor_id` int(11) NOT NULL,
  `idusuario_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tractor_tractor`
--

INSERT INTO `tractor_tractor` (`idtractor`, `nrotractor`, `horainicial`, `horauso`, `estado`, `estado_actividad`, `idfundo_id`, `idtipotractor_id`, `idusuario_id`) VALUES
(1, 'VIÑATERO1', 100, 0, 1, 1, 1, 1, 1),
(2, 'VIÑATERO2', 114, 14, 1, 1, 1, 1, 1),
(3, 'VIÑATERO3', 100, 0, 1, 1, 3, 1, 1),
(4, 'VIÑATERO4', 100, 0, 1, 1, 3, 1, 2),
(5, 'VIÑATERO5', 100, 0, 1, 1, 4, 1, 2),
(6, 'VIÑATERO6', 100, 0, 1, 1, 4, 1, 2),
(7, 'DOBLE1', 110, 10, 1, 1, 1, 2, 1),
(8, 'DOBLE2', 100, 0, 1, 1, 1, 2, 1),
(9, 'DOBLE3', 100, 0, 1, 1, 3, 2, 1),
(10, 'DOBLE4', 110, 10, 1, 1, 3, 2, 2),
(11, 'DOBLE5', 100, 0, 1, 1, 4, 2, 2),
(12, 'DOBLE6', 100, 0, 1, 1, 4, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_persona`
--

CREATE TABLE `usuario_persona` (
  `idpersona` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `dni` varchar(8) DEFAULT NULL,
  `codigo` varchar(12) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_persona`
--

INSERT INTO `usuario_persona` (`idpersona`, `nombres`, `apellidos`, `dni`, `codigo`, `estado`, `creado_en`, `actualizado_en`) VALUES
(1, 'Carlos', 'Gómez', '12345678', '10000', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(2, 'María', 'Pérez', '87654321', '10001', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(3, 'Luis', 'Rodríguez', '11223344', '10002', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(4, 'Ana', 'López', '44332211', '10003', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(5, 'Jorge', 'Martínez', '55667788', '10004', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(6, 'Elena', 'García', '99887766', '10005', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(7, 'Pedro', 'Fernández', '66778899', '10006', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(8, 'Laura', 'Sánchez', '33445566', '10007', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(9, 'Juan', 'Ramírez', '77889900', '10008', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(10, 'Marta', 'Torres', '41556677', '10009', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(11, 'Miguel', 'Pachas', '42556677', '10010', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(12, 'Diego', 'Pauca', '43556677', '10011', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(13, 'Piero', 'Herrera', '14556677', '10012', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(14, 'Ronaldo', 'Yataco', '34556677', '10013', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(15, 'Brayan', 'Palomino', '64556677', '10014', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(16, 'Marcos', 'Medina', '45556677', '10015', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(17, 'Julio', 'Martínez', '46556677', '10016', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(18, 'Jhon', 'Campos', '47556677', '10017', 1, '0000-00-00 00:00:00.000000', '0000-00-00'),
(19, 'kevin', 'Torres', '48556677', '10018', 1, '0000-00-00 00:00:00.000000', '0000-00-00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_rol`
--

CREATE TABLE `usuario_rol` (
  `idrol` int(11) NOT NULL,
  `rol` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_rol`
--

INSERT INTO `usuario_rol` (`idrol`, `rol`, `estado`) VALUES
(1, 'Asistente', 1),
(2, 'Admin', 1),
(3, 'Supervisor', 1),
(4, 'Gerencia', 1),
(5, 'Mecanico', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_usuario`
--

CREATE TABLE `usuario_usuario` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `idrol_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_usuario`
--

INSERT INTO `usuario_usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `idrol_id`) VALUES
(1, 'pbkdf2_sha256$600000$TfrbuIfPUV4tFgKlAcUe8a$XmhyTwJsxAqr4EL+Ya2A+pl8yg58KJVPlVO3il07JO8=', '2024-06-04 22:29:07.993373', 1, 'Angel', 'Angel', 'pachas', '', 1, 1, '2024-06-04 19:01:04.000000', 3),
(2, 'pbkdf2_sha256$600000$M7V7LwRbbNU0mBtN5vslx7$iHFm3s4BRRLlwDW0sbemtDRqK+EFFonW0VVcKIzyYbM=', '2024-06-04 21:05:48.530075', 0, 'Luis', 'Luis', 'llancari', '', 0, 1, '2024-06-04 19:18:30.975621', 3),
(3, 'pbkdf2_sha256$600000$C0IN9Q4nxAvLJJX7yUX02T$ppOUWZ8rfIceoImm/BRFBeylFFp2AKjkJBKmDcdCqsg=', NULL, 0, 'harold', 'harold', 'Quispe', '', 0, 0, '2024-06-04 19:24:20.302956', 3),
(4, 'pbkdf2_sha256$600000$Wvuu0HpvRiViQ6UAimlkN2$kBodd3XWSobFT+kC3t1e/iG5eig0n5fMjplvXV53BHw=', '2024-06-04 20:46:35.092638', 0, 'efrain', 'efrain', 'Quispe', '', 0, 1, '2024-06-04 19:26:06.549934', 2),
(5, 'pbkdf2_sha256$600000$QdYwNc0UsD4o8XvleD7Ptc$QzH0J7d4hQnMuKuSguX1SN50a8ib8VrlcxW2dxCgshc=', '2024-06-04 20:48:54.356478', 0, 'pedro', 'pedro', 'Chavez', '', 0, 1, '2024-06-04 19:26:54.504092', 1),
(6, 'pbkdf2_sha256$600000$WbU3F4fOE2pZmFEMGHF6cH$OYxeHNUUK1RfS5yaNwQOLks0lJmo01PH+94eSjTnw48=', '2024-06-04 21:31:56.836974', 0, 'maria', 'maria', 'Herrera', '', 0, 1, '2024-06-04 19:29:54.979786', 4),
(7, 'pbkdf2_sha256$600000$DOC16nPLgZx01O60nqb2e8$HdW/Cunnj3bpn3x3FD30cTC4DjgIzWCn4DgbojnjyxQ=', '2024-06-04 21:44:01.571470', 0, 'Juan', 'Juan', 'torres', '', 0, 1, '2024-06-04 19:35:57.039437', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_usuario_groups`
--

CREATE TABLE `usuario_usuario_groups` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_usuario_user_permissions`
--

CREATE TABLE `usuario_usuario_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `ceco_ceco`
--
ALTER TABLE `ceco_ceco`
  ADD PRIMARY KEY (`idceco`);

--
-- Indices de la tabla `componente_pieza_componente`
--
ALTER TABLE `componente_pieza_componente`
  ADD PRIMARY KEY (`idcomponente`),
  ADD UNIQUE KEY `componente` (`componente`),
  ADD UNIQUE KEY `codcomponente` (`codcomponente`),
  ADD KEY `componente_pieza_com_idsistema_id_1ae99d54_fk_component` (`idsistema_id`);

--
-- Indices de la tabla `componente_pieza_configuraciontipoimplemento`
--
ALTER TABLE `componente_pieza_configuraciontipoimplemento`
  ADD PRIMARY KEY (`idconfiguraciontipoimplemento`);

--
-- Indices de la tabla `componente_pieza_detallecomponente`
--
ALTER TABLE `componente_pieza_detallecomponente`
  ADD PRIMARY KEY (`iddetallecomponente`),
  ADD KEY `componente_pieza_det_idcomponente_id_d3ce300f_fk_component` (`idcomponente_id`),
  ADD KEY `componente_pieza_det_idpieza_id_58ce19dc_fk_component` (`idpieza_id`);

--
-- Indices de la tabla `componente_pieza_detalleconfiguracion`
--
ALTER TABLE `componente_pieza_detalleconfiguracion`
  ADD PRIMARY KEY (`iddetallecomponente`),
  ADD KEY `componente_pieza_det_idcomponente_id_0d20b29f_fk_component` (`idcomponente_id`),
  ADD KEY `componente_pieza_det_idconfiguracion_id_2aaf2fc2_fk_component` (`idconfiguracion_id`);

--
-- Indices de la tabla `componente_pieza_pieza`
--
ALTER TABLE `componente_pieza_pieza`
  ADD PRIMARY KEY (`idpieza`);

--
-- Indices de la tabla `componente_pieza_sistema`
--
ALTER TABLE `componente_pieza_sistema`
  ADD PRIMARY KEY (`idsistema`),
  ADD UNIQUE KEY `sistema` (`sistema`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_usuario_usuario_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `fundo_cultivo_cultivo`
--
ALTER TABLE `fundo_cultivo_cultivo`
  ADD PRIMARY KEY (`idcultivo`);

--
-- Indices de la tabla `fundo_cultivo_fundo`
--
ALTER TABLE `fundo_cultivo_fundo`
  ADD PRIMARY KEY (`idfundo`),
  ADD KEY `fundo_cultivo_fundo_idsede_id_851fd8ba_fk_localizac` (`idsede_id`);

--
-- Indices de la tabla `fundo_cultivo_lote`
--
ALTER TABLE `fundo_cultivo_lote`
  ADD PRIMARY KEY (`idlote`),
  ADD KEY `fundo_cultivo_lote_idfundo_id_782ab9a9_fk_fundo_cul` (`idfundo_id`),
  ADD KEY `fundo_cultivo_lote_idvariedad_id_dd79a52c_fk_fundo_cul` (`idvariedad_id`);

--
-- Indices de la tabla `fundo_cultivo_variedad`
--
ALTER TABLE `fundo_cultivo_variedad`
  ADD PRIMARY KEY (`idvariedad`),
  ADD KEY `fundo_cultivo_varied_idcultivo_id_bc5e5851_fk_fundo_cul` (`idcultivo_id`);

--
-- Indices de la tabla `implemento_detimplementos`
--
ALTER TABLE `implemento_detimplementos`
  ADD PRIMARY KEY (`iddetalleimplemento`),
  ADD KEY `implemento_detimplem_iddetallecomponente__44267bb3_fk_component` (`iddetallecomponente_id`),
  ADD KEY `implemento_detimplem_idimplemento_id_4fa089b3_fk_implement` (`idimplemento_id`);

--
-- Indices de la tabla `implemento_implemento`
--
ALTER TABLE `implemento_implemento`
  ADD PRIMARY KEY (`idimplemento`),
  ADD KEY `implemento_implemento_idceco_id_2c850f10_fk_ceco_ceco_idceco` (`idceco_id`),
  ADD KEY `implemento_implement_idtipoimplemento_id_5fd9fe6e_fk_implement` (`idtipoimplemento_id`),
  ADD KEY `implemento_implement_idusuario_id_38219cf9_fk_usuario_u` (`idusuario_id`);

--
-- Indices de la tabla `implemento_tipoimplemento`
--
ALTER TABLE `implemento_tipoimplemento`
  ADD PRIMARY KEY (`idtipoimplemento`),
  ADD KEY `implemento_tipoimple_idconfiguracion_impl_5ac71684_fk_component` (`idconfiguracion_implemento_id`);

--
-- Indices de la tabla `localizacion_area`
--
ALTER TABLE `localizacion_area`
  ADD PRIMARY KEY (`idarea`),
  ADD KEY `localizacion_area_idbase_id_a3b5a3d8_fk_localizacion_base_idbase` (`idbase_id`);

--
-- Indices de la tabla `localizacion_base`
--
ALTER TABLE `localizacion_base`
  ADD PRIMARY KEY (`idbase`),
  ADD KEY `localizacion_base_idsede_id_77bd1418_fk_localizacion_sede_idsede` (`idsede_id`);

--
-- Indices de la tabla `localizacion_sede`
--
ALTER TABLE `localizacion_sede`
  ADD PRIMARY KEY (`idsede`);

--
-- Indices de la tabla `mantenimiento_acciones`
--
ALTER TABLE `mantenimiento_acciones`
  ADD PRIMARY KEY (`idaccion`),
  ADD UNIQUE KEY `accion` (`accion`);

--
-- Indices de la tabla `mantenimiento_detallecambios`
--
ALTER TABLE `mantenimiento_detallecambios`
  ADD PRIMARY KEY (`iddetallecambio`),
  ADD KEY `mantenimiento_detall_iddetalleimplemento__386ba28e_fk_implement` (`iddetalleimplemento_id`),
  ADD KEY `mantenimiento_detall_idmantenimiento_id_1bc840f3_fk_mantenimi` (`idmantenimiento_id`);

--
-- Indices de la tabla `mantenimiento_detallemantenimiento`
--
ALTER TABLE `mantenimiento_detallemantenimiento`
  ADD PRIMARY KEY (`iddetallemantenimiento`),
  ADD KEY `mantenimiento_detall_idaccion_id_eebddaa4_fk_mantenimi` (`idaccion_id`),
  ADD KEY `mantenimiento_detall_idmantenimiento_id_6a4cd3e7_fk_mantenimi` (`idmantenimiento_id`);

--
-- Indices de la tabla `mantenimiento_detmotivos`
--
ALTER TABLE `mantenimiento_detmotivos`
  ADD PRIMARY KEY (`iddetmotivo`),
  ADD KEY `mantenimiento_detmot_idaccion_id_7c5b4eea_fk_mantenimi` (`idaccion_id`),
  ADD KEY `mantenimiento_detmot_idprogramacionmanten_e6ea84e7_fk_mantenimi` (`idprogramacionmantenimiento_id`);

--
-- Indices de la tabla `mantenimiento_diagnostico`
--
ALTER TABLE `mantenimiento_diagnostico`
  ADD PRIMARY KEY (`iddiagnostico`);

--
-- Indices de la tabla `mantenimiento_mantenimiento`
--
ALTER TABLE `mantenimiento_mantenimiento`
  ADD PRIMARY KEY (`idmantenimiento`),
  ADD KEY `mantenimiento_manten_idprogramacionmanten_8f9c833c_fk_mantenimi` (`idprogramacionmantenimiento_id`),
  ADD KEY `mantenimiento_manten_idencargado_id_4d184025_fk_operarios` (`idencargado_id`);

--
-- Indices de la tabla `mantenimiento_programacionmantenimiento`
--
ALTER TABLE `mantenimiento_programacionmantenimiento`
  ADD PRIMARY KEY (`idprogramacionmantenimiento`),
  ADD KEY `mantenimiento_progra_idimplemento_id_de95d60c_fk_implement` (`idimplemento_id`);

--
-- Indices de la tabla `mantenimiento_recambios`
--
ALTER TABLE `mantenimiento_recambios`
  ADD PRIMARY KEY (`idrecambio`),
  ADD KEY `mantenimiento_recamb_idmantenimiento_id_dc62d069_fk_mantenimi` (`idmantenimiento_id`);

--
-- Indices de la tabla `operarios_encargado`
--
ALTER TABLE `operarios_encargado`
  ADD PRIMARY KEY (`idencargado`),
  ADD KEY `operarios_encargado_idpersona_id_d9296768_fk_usuario_p` (`idpersona_id`);

--
-- Indices de la tabla `operarios_solicitante`
--
ALTER TABLE `operarios_solicitante`
  ADD PRIMARY KEY (`idsolicitante`),
  ADD KEY `operarios_solicitant_idpersona_id_1df0ebb2_fk_usuario_p` (`idpersona_id`),
  ADD KEY `operarios_solicitant_idtiposolicitante_id_2872a957_fk_operarios` (`idtiposolicitante_id`);

--
-- Indices de la tabla `operarios_tiposolicitante`
--
ALTER TABLE `operarios_tiposolicitante`
  ADD PRIMARY KEY (`idtiposolicitante`);

--
-- Indices de la tabla `operarios_tractorista`
--
ALTER TABLE `operarios_tractorista`
  ADD PRIMARY KEY (`idtractorista`),
  ADD KEY `operarios_tractorist_idpersona_id_8fdce615_fk_usuario_p` (`idpersona_id`),
  ADD KEY `operarios_tractorist_idusuario_id_7e2d2b2a_fk_usuario_u` (`idusuario_id`);

--
-- Indices de la tabla `programacion_labor_detallelabor`
--
ALTER TABLE `programacion_labor_detallelabor`
  ADD PRIMARY KEY (`iddetlabor`),
  ADD KEY `programacion_labor_d_idimplemento_id_5d5249e8_fk_implement` (`idimplemento_id`),
  ADD KEY `programacion_labor_d_idprogramacion_id_45a2f05e_fk_programac` (`idprogramacion_id`);

--
-- Indices de la tabla `programacion_labor_programacion`
--
ALTER TABLE `programacion_labor_programacion`
  ADD PRIMARY KEY (`idprogramacion`),
  ADD KEY `programacion_labor_p_idlote_id_dc4e23be_fk_fundo_cul` (`idlote_id`),
  ADD KEY `programacion_labor_p_idsolicitante_id_a31618cc_fk_operarios` (`idsolicitante_id`),
  ADD KEY `programacion_labor_p_idtipolabor_id_b186c544_fk_programac` (`idtipolabor_id`),
  ADD KEY `programacion_labor_p_idtractor_id_a33a869d_fk_tractor_t` (`idtractor_id`),
  ADD KEY `programacion_labor_p_idtractorista_id_b6325322_fk_operarios` (`idtractorista_id`),
  ADD KEY `programacion_labor_p_idusuario_id_47e7e415_fk_usuario_u` (`idusuario_id`);

--
-- Indices de la tabla `programacion_labor_tipolabor`
--
ALTER TABLE `programacion_labor_tipolabor`
  ADD PRIMARY KEY (`idtipolabor`),
  ADD UNIQUE KEY `tipolabor` (`tipolabor`);

--
-- Indices de la tabla `tractor_reportetractor`
--
ALTER TABLE `tractor_reportetractor`
  ADD PRIMARY KEY (`idreportetractor`),
  ADD UNIQUE KEY `correlativo` (`correlativo`),
  ADD KEY `tractor_reportetract_idprogramacion_id_38bbcdaf_fk_programac` (`idprogramacion_id`),
  ADD KEY `tractor_reportetract_idusuario_id_61d154d3_fk_usuario_u` (`idusuario_id`);

--
-- Indices de la tabla `tractor_tipotractor`
--
ALTER TABLE `tractor_tipotractor`
  ADD PRIMARY KEY (`idtipotractor`);

--
-- Indices de la tabla `tractor_tractor`
--
ALTER TABLE `tractor_tractor`
  ADD PRIMARY KEY (`idtractor`),
  ADD KEY `tractor_tractor_idfundo_id_7c9f50e5_fk_fundo_cul` (`idfundo_id`),
  ADD KEY `tractor_tractor_idtipotractor_id_e0cf7d46_fk_tractor_t` (`idtipotractor_id`),
  ADD KEY `tractor_tractor_idusuario_id_6e5caf82_fk_usuario_usuario_id` (`idusuario_id`);

--
-- Indices de la tabla `usuario_persona`
--
ALTER TABLE `usuario_persona`
  ADD PRIMARY KEY (`idpersona`),
  ADD UNIQUE KEY `dni` (`dni`);

--
-- Indices de la tabla `usuario_rol`
--
ALTER TABLE `usuario_rol`
  ADD PRIMARY KEY (`idrol`),
  ADD UNIQUE KEY `rol` (`rol`);

--
-- Indices de la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `usuario_usuario_idrol_id_7a89f89f_fk_usuario_rol_idrol` (`idrol_id`);

--
-- Indices de la tabla `usuario_usuario_groups`
--
ALTER TABLE `usuario_usuario_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_usuario_groups_usuario_id_group_id_a4cfb0b8_uniq` (`usuario_id`,`group_id`),
  ADD KEY `usuario_usuario_groups_group_id_b9c090f8_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `usuario_usuario_user_permissions`
--
ALTER TABLE `usuario_usuario_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_usuario_user_per_usuario_id_permission_id_c0a85055_uniq` (`usuario_id`,`permission_id`),
  ADD KEY `usuario_usuario_user_permission_id_5cad0a4b_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=173;

--
-- AUTO_INCREMENT de la tabla `ceco_ceco`
--
ALTER TABLE `ceco_ceco`
  MODIFY `idceco` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_componente`
--
ALTER TABLE `componente_pieza_componente`
  MODIFY `idcomponente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_configuraciontipoimplemento`
--
ALTER TABLE `componente_pieza_configuraciontipoimplemento`
  MODIFY `idconfiguraciontipoimplemento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_detallecomponente`
--
ALTER TABLE `componente_pieza_detallecomponente`
  MODIFY `iddetallecomponente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_detalleconfiguracion`
--
ALTER TABLE `componente_pieza_detalleconfiguracion`
  MODIFY `iddetallecomponente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_pieza`
--
ALTER TABLE `componente_pieza_pieza`
  MODIFY `idpieza` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_sistema`
--
ALTER TABLE `componente_pieza_sistema`
  MODIFY `idsistema` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_cultivo`
--
ALTER TABLE `fundo_cultivo_cultivo`
  MODIFY `idcultivo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_fundo`
--
ALTER TABLE `fundo_cultivo_fundo`
  MODIFY `idfundo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_lote`
--
ALTER TABLE `fundo_cultivo_lote`
  MODIFY `idlote` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_variedad`
--
ALTER TABLE `fundo_cultivo_variedad`
  MODIFY `idvariedad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `implemento_detimplementos`
--
ALTER TABLE `implemento_detimplementos`
  MODIFY `iddetalleimplemento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de la tabla `implemento_implemento`
--
ALTER TABLE `implemento_implemento`
  MODIFY `idimplemento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `implemento_tipoimplemento`
--
ALTER TABLE `implemento_tipoimplemento`
  MODIFY `idtipoimplemento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `localizacion_area`
--
ALTER TABLE `localizacion_area`
  MODIFY `idarea` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `localizacion_base`
--
ALTER TABLE `localizacion_base`
  MODIFY `idbase` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `localizacion_sede`
--
ALTER TABLE `localizacion_sede`
  MODIFY `idsede` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_acciones`
--
ALTER TABLE `mantenimiento_acciones`
  MODIFY `idaccion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_detallecambios`
--
ALTER TABLE `mantenimiento_detallecambios`
  MODIFY `iddetallecambio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_detallemantenimiento`
--
ALTER TABLE `mantenimiento_detallemantenimiento`
  MODIFY `iddetallemantenimiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_detmotivos`
--
ALTER TABLE `mantenimiento_detmotivos`
  MODIFY `iddetmotivo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_diagnostico`
--
ALTER TABLE `mantenimiento_diagnostico`
  MODIFY `iddiagnostico` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_mantenimiento`
--
ALTER TABLE `mantenimiento_mantenimiento`
  MODIFY `idmantenimiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_programacionmantenimiento`
--
ALTER TABLE `mantenimiento_programacionmantenimiento`
  MODIFY `idprogramacionmantenimiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `mantenimiento_recambios`
--
ALTER TABLE `mantenimiento_recambios`
  MODIFY `idrecambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `operarios_encargado`
--
ALTER TABLE `operarios_encargado`
  MODIFY `idencargado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `operarios_solicitante`
--
ALTER TABLE `operarios_solicitante`
  MODIFY `idsolicitante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `operarios_tiposolicitante`
--
ALTER TABLE `operarios_tiposolicitante`
  MODIFY `idtiposolicitante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `operarios_tractorista`
--
ALTER TABLE `operarios_tractorista`
  MODIFY `idtractorista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `programacion_labor_detallelabor`
--
ALTER TABLE `programacion_labor_detallelabor`
  MODIFY `iddetlabor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `programacion_labor_programacion`
--
ALTER TABLE `programacion_labor_programacion`
  MODIFY `idprogramacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `programacion_labor_tipolabor`
--
ALTER TABLE `programacion_labor_tipolabor`
  MODIFY `idtipolabor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `tractor_reportetractor`
--
ALTER TABLE `tractor_reportetractor`
  MODIFY `idreportetractor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tractor_tipotractor`
--
ALTER TABLE `tractor_tipotractor`
  MODIFY `idtipotractor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tractor_tractor`
--
ALTER TABLE `tractor_tractor`
  MODIFY `idtractor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuario_persona`
--
ALTER TABLE `usuario_persona`
  MODIFY `idpersona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `usuario_rol`
--
ALTER TABLE `usuario_rol`
  MODIFY `idrol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `usuario_usuario_groups`
--
ALTER TABLE `usuario_usuario_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario_usuario_user_permissions`
--
ALTER TABLE `usuario_usuario_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `componente_pieza_componente`
--
ALTER TABLE `componente_pieza_componente`
  ADD CONSTRAINT `componente_pieza_com_idsistema_id_1ae99d54_fk_component` FOREIGN KEY (`idsistema_id`) REFERENCES `componente_pieza_sistema` (`idsistema`);

--
-- Filtros para la tabla `componente_pieza_detallecomponente`
--
ALTER TABLE `componente_pieza_detallecomponente`
  ADD CONSTRAINT `componente_pieza_det_idcomponente_id_d3ce300f_fk_component` FOREIGN KEY (`idcomponente_id`) REFERENCES `componente_pieza_componente` (`idcomponente`),
  ADD CONSTRAINT `componente_pieza_det_idpieza_id_58ce19dc_fk_component` FOREIGN KEY (`idpieza_id`) REFERENCES `componente_pieza_pieza` (`idpieza`);

--
-- Filtros para la tabla `componente_pieza_detalleconfiguracion`
--
ALTER TABLE `componente_pieza_detalleconfiguracion`
  ADD CONSTRAINT `componente_pieza_det_idcomponente_id_0d20b29f_fk_component` FOREIGN KEY (`idcomponente_id`) REFERENCES `componente_pieza_componente` (`idcomponente`),
  ADD CONSTRAINT `componente_pieza_det_idconfiguracion_id_2aaf2fc2_fk_component` FOREIGN KEY (`idconfiguracion_id`) REFERENCES `componente_pieza_configuraciontipoimplemento` (`idconfiguraciontipoimplemento`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Filtros para la tabla `fundo_cultivo_fundo`
--
ALTER TABLE `fundo_cultivo_fundo`
  ADD CONSTRAINT `fundo_cultivo_fundo_idsede_id_851fd8ba_fk_localizac` FOREIGN KEY (`idsede_id`) REFERENCES `localizacion_sede` (`idsede`);

--
-- Filtros para la tabla `fundo_cultivo_lote`
--
ALTER TABLE `fundo_cultivo_lote`
  ADD CONSTRAINT `fundo_cultivo_lote_idfundo_id_782ab9a9_fk_fundo_cul` FOREIGN KEY (`idfundo_id`) REFERENCES `fundo_cultivo_fundo` (`idfundo`),
  ADD CONSTRAINT `fundo_cultivo_lote_idvariedad_id_dd79a52c_fk_fundo_cul` FOREIGN KEY (`idvariedad_id`) REFERENCES `fundo_cultivo_variedad` (`idvariedad`);

--
-- Filtros para la tabla `fundo_cultivo_variedad`
--
ALTER TABLE `fundo_cultivo_variedad`
  ADD CONSTRAINT `fundo_cultivo_varied_idcultivo_id_bc5e5851_fk_fundo_cul` FOREIGN KEY (`idcultivo_id`) REFERENCES `fundo_cultivo_cultivo` (`idcultivo`);

--
-- Filtros para la tabla `implemento_detimplementos`
--
ALTER TABLE `implemento_detimplementos`
  ADD CONSTRAINT `implemento_detimplem_iddetallecomponente__44267bb3_fk_component` FOREIGN KEY (`iddetallecomponente_id`) REFERENCES `componente_pieza_detallecomponente` (`iddetallecomponente`),
  ADD CONSTRAINT `implemento_detimplem_idimplemento_id_4fa089b3_fk_implement` FOREIGN KEY (`idimplemento_id`) REFERENCES `implemento_implemento` (`idimplemento`);

--
-- Filtros para la tabla `implemento_implemento`
--
ALTER TABLE `implemento_implemento`
  ADD CONSTRAINT `implemento_implement_idtipoimplemento_id_5fd9fe6e_fk_implement` FOREIGN KEY (`idtipoimplemento_id`) REFERENCES `implemento_tipoimplemento` (`idtipoimplemento`),
  ADD CONSTRAINT `implemento_implement_idusuario_id_38219cf9_fk_usuario_u` FOREIGN KEY (`idusuario_id`) REFERENCES `usuario_usuario` (`id`),
  ADD CONSTRAINT `implemento_implemento_idceco_id_2c850f10_fk_ceco_ceco_idceco` FOREIGN KEY (`idceco_id`) REFERENCES `ceco_ceco` (`idceco`);

--
-- Filtros para la tabla `implemento_tipoimplemento`
--
ALTER TABLE `implemento_tipoimplemento`
  ADD CONSTRAINT `implemento_tipoimple_idconfiguracion_impl_5ac71684_fk_component` FOREIGN KEY (`idconfiguracion_implemento_id`) REFERENCES `componente_pieza_configuraciontipoimplemento` (`idconfiguraciontipoimplemento`);

--
-- Filtros para la tabla `localizacion_area`
--
ALTER TABLE `localizacion_area`
  ADD CONSTRAINT `localizacion_area_idbase_id_a3b5a3d8_fk_localizacion_base_idbase` FOREIGN KEY (`idbase_id`) REFERENCES `localizacion_base` (`idbase`);

--
-- Filtros para la tabla `localizacion_base`
--
ALTER TABLE `localizacion_base`
  ADD CONSTRAINT `localizacion_base_idsede_id_77bd1418_fk_localizacion_sede_idsede` FOREIGN KEY (`idsede_id`) REFERENCES `localizacion_sede` (`idsede`);

--
-- Filtros para la tabla `mantenimiento_detallecambios`
--
ALTER TABLE `mantenimiento_detallecambios`
  ADD CONSTRAINT `mantenimiento_detall_iddetalleimplemento__386ba28e_fk_implement` FOREIGN KEY (`iddetalleimplemento_id`) REFERENCES `implemento_detimplementos` (`iddetalleimplemento`),
  ADD CONSTRAINT `mantenimiento_detall_idmantenimiento_id_1bc840f3_fk_mantenimi` FOREIGN KEY (`idmantenimiento_id`) REFERENCES `mantenimiento_mantenimiento` (`idmantenimiento`);

--
-- Filtros para la tabla `mantenimiento_detallemantenimiento`
--
ALTER TABLE `mantenimiento_detallemantenimiento`
  ADD CONSTRAINT `mantenimiento_detall_idaccion_id_eebddaa4_fk_mantenimi` FOREIGN KEY (`idaccion_id`) REFERENCES `mantenimiento_acciones` (`idaccion`),
  ADD CONSTRAINT `mantenimiento_detall_idmantenimiento_id_6a4cd3e7_fk_mantenimi` FOREIGN KEY (`idmantenimiento_id`) REFERENCES `mantenimiento_mantenimiento` (`idmantenimiento`);

--
-- Filtros para la tabla `mantenimiento_detmotivos`
--
ALTER TABLE `mantenimiento_detmotivos`
  ADD CONSTRAINT `mantenimiento_detmot_idaccion_id_7c5b4eea_fk_mantenimi` FOREIGN KEY (`idaccion_id`) REFERENCES `mantenimiento_acciones` (`idaccion`),
  ADD CONSTRAINT `mantenimiento_detmot_idprogramacionmanten_e6ea84e7_fk_mantenimi` FOREIGN KEY (`idprogramacionmantenimiento_id`) REFERENCES `mantenimiento_programacionmantenimiento` (`idprogramacionmantenimiento`);

--
-- Filtros para la tabla `mantenimiento_mantenimiento`
--
ALTER TABLE `mantenimiento_mantenimiento`
  ADD CONSTRAINT `mantenimiento_manten_idencargado_id_4d184025_fk_operarios` FOREIGN KEY (`idencargado_id`) REFERENCES `operarios_encargado` (`idencargado`),
  ADD CONSTRAINT `mantenimiento_manten_idprogramacionmanten_8f9c833c_fk_mantenimi` FOREIGN KEY (`idprogramacionmantenimiento_id`) REFERENCES `mantenimiento_programacionmantenimiento` (`idprogramacionmantenimiento`);

--
-- Filtros para la tabla `mantenimiento_programacionmantenimiento`
--
ALTER TABLE `mantenimiento_programacionmantenimiento`
  ADD CONSTRAINT `mantenimiento_progra_idimplemento_id_de95d60c_fk_implement` FOREIGN KEY (`idimplemento_id`) REFERENCES `implemento_implemento` (`idimplemento`);

--
-- Filtros para la tabla `mantenimiento_recambios`
--
ALTER TABLE `mantenimiento_recambios`
  ADD CONSTRAINT `mantenimiento_recamb_idmantenimiento_id_dc62d069_fk_mantenimi` FOREIGN KEY (`idmantenimiento_id`) REFERENCES `mantenimiento_mantenimiento` (`idmantenimiento`);

--
-- Filtros para la tabla `operarios_encargado`
--
ALTER TABLE `operarios_encargado`
  ADD CONSTRAINT `operarios_encargado_idpersona_id_d9296768_fk_usuario_p` FOREIGN KEY (`idpersona_id`) REFERENCES `usuario_persona` (`idpersona`);

--
-- Filtros para la tabla `operarios_solicitante`
--
ALTER TABLE `operarios_solicitante`
  ADD CONSTRAINT `operarios_solicitant_idpersona_id_1df0ebb2_fk_usuario_p` FOREIGN KEY (`idpersona_id`) REFERENCES `usuario_persona` (`idpersona`),
  ADD CONSTRAINT `operarios_solicitant_idtiposolicitante_id_2872a957_fk_operarios` FOREIGN KEY (`idtiposolicitante_id`) REFERENCES `operarios_tiposolicitante` (`idtiposolicitante`);

--
-- Filtros para la tabla `operarios_tractorista`
--
ALTER TABLE `operarios_tractorista`
  ADD CONSTRAINT `operarios_tractorist_idpersona_id_8fdce615_fk_usuario_p` FOREIGN KEY (`idpersona_id`) REFERENCES `usuario_persona` (`idpersona`),
  ADD CONSTRAINT `operarios_tractorist_idusuario_id_7e2d2b2a_fk_usuario_u` FOREIGN KEY (`idusuario_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Filtros para la tabla `programacion_labor_detallelabor`
--
ALTER TABLE `programacion_labor_detallelabor`
  ADD CONSTRAINT `programacion_labor_d_idimplemento_id_5d5249e8_fk_implement` FOREIGN KEY (`idimplemento_id`) REFERENCES `implemento_implemento` (`idimplemento`),
  ADD CONSTRAINT `programacion_labor_d_idprogramacion_id_45a2f05e_fk_programac` FOREIGN KEY (`idprogramacion_id`) REFERENCES `programacion_labor_programacion` (`idprogramacion`);

--
-- Filtros para la tabla `programacion_labor_programacion`
--
ALTER TABLE `programacion_labor_programacion`
  ADD CONSTRAINT `programacion_labor_p_idlote_id_dc4e23be_fk_fundo_cul` FOREIGN KEY (`idlote_id`) REFERENCES `fundo_cultivo_lote` (`idlote`),
  ADD CONSTRAINT `programacion_labor_p_idsolicitante_id_a31618cc_fk_operarios` FOREIGN KEY (`idsolicitante_id`) REFERENCES `operarios_solicitante` (`idsolicitante`),
  ADD CONSTRAINT `programacion_labor_p_idtipolabor_id_b186c544_fk_programac` FOREIGN KEY (`idtipolabor_id`) REFERENCES `programacion_labor_tipolabor` (`idtipolabor`),
  ADD CONSTRAINT `programacion_labor_p_idtractor_id_a33a869d_fk_tractor_t` FOREIGN KEY (`idtractor_id`) REFERENCES `tractor_tractor` (`idtractor`),
  ADD CONSTRAINT `programacion_labor_p_idtractorista_id_b6325322_fk_operarios` FOREIGN KEY (`idtractorista_id`) REFERENCES `operarios_tractorista` (`idtractorista`),
  ADD CONSTRAINT `programacion_labor_p_idusuario_id_47e7e415_fk_usuario_u` FOREIGN KEY (`idusuario_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Filtros para la tabla `tractor_reportetractor`
--
ALTER TABLE `tractor_reportetractor`
  ADD CONSTRAINT `tractor_reportetract_idprogramacion_id_38bbcdaf_fk_programac` FOREIGN KEY (`idprogramacion_id`) REFERENCES `programacion_labor_programacion` (`idprogramacion`),
  ADD CONSTRAINT `tractor_reportetract_idusuario_id_61d154d3_fk_usuario_u` FOREIGN KEY (`idusuario_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Filtros para la tabla `tractor_tractor`
--
ALTER TABLE `tractor_tractor`
  ADD CONSTRAINT `tractor_tractor_idfundo_id_7c9f50e5_fk_fundo_cul` FOREIGN KEY (`idfundo_id`) REFERENCES `fundo_cultivo_fundo` (`idfundo`),
  ADD CONSTRAINT `tractor_tractor_idtipotractor_id_e0cf7d46_fk_tractor_t` FOREIGN KEY (`idtipotractor_id`) REFERENCES `tractor_tipotractor` (`idtipotractor`),
  ADD CONSTRAINT `tractor_tractor_idusuario_id_6e5caf82_fk_usuario_usuario_id` FOREIGN KEY (`idusuario_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Filtros para la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  ADD CONSTRAINT `usuario_usuario_idrol_id_7a89f89f_fk_usuario_rol_idrol` FOREIGN KEY (`idrol_id`) REFERENCES `usuario_rol` (`idrol`);

--
-- Filtros para la tabla `usuario_usuario_groups`
--
ALTER TABLE `usuario_usuario_groups`
  ADD CONSTRAINT `usuario_usuario_groups_group_id_b9c090f8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `usuario_usuario_groups_usuario_id_62de76a1_fk_usuario_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Filtros para la tabla `usuario_usuario_user_permissions`
--
ALTER TABLE `usuario_usuario_user_permissions`
  ADD CONSTRAINT `usuario_usuario_user_permission_id_5cad0a4b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `usuario_usuario_user_usuario_id_5969a193_fk_usuario_u` FOREIGN KEY (`usuario_id`) REFERENCES `usuario_usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
