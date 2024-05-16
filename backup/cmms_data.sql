-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-05-2024 a las 19:19:28
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(89, 'Can add Sistema', 23, 'add_sistema'),
(90, 'Can change Sistema', 23, 'change_sistema'),
(91, 'Can delete Sistema', 23, 'delete_sistema'),
(92, 'Can view Sistema', 23, 'view_sistema'),
(93, 'Can add Pieza', 24, 'add_pieza'),
(94, 'Can change Pieza', 24, 'change_pieza'),
(95, 'Can delete Pieza', 24, 'delete_pieza'),
(96, 'Can view Pieza', 24, 'view_pieza'),
(97, 'Can add Solicitante', 25, 'add_solicitante'),
(98, 'Can change Solicitante', 25, 'change_solicitante'),
(99, 'Can delete Solicitante', 25, 'delete_solicitante'),
(100, 'Can view Solicitante', 25, 'view_solicitante'),
(101, 'Can add Tipo Solicitante', 26, 'add_tiposolicitante'),
(102, 'Can change Tipo Solicitante', 26, 'change_tiposolicitante'),
(103, 'Can delete Tipo Solicitante', 26, 'delete_tiposolicitante'),
(104, 'Can view Tipo Solicitante', 26, 'view_tiposolicitante'),
(105, 'Can add Tractorista', 27, 'add_tractorista'),
(106, 'Can change Tractorista', 27, 'change_tractorista'),
(107, 'Can delete Tractorista', 27, 'delete_tractorista'),
(108, 'Can view Tractorista', 27, 'view_tractorista'),
(109, 'Can add Detalle Labor', 28, 'add_detallelabor'),
(110, 'Can change Detalle Labor', 28, 'change_detallelabor'),
(111, 'Can delete Detalle Labor', 28, 'delete_detallelabor'),
(112, 'Can view Detalle Labor', 28, 'view_detallelabor'),
(113, 'Can add Tipo de labor', 29, 'add_tipolabor'),
(114, 'Can change Tipo de labor', 29, 'change_tipolabor'),
(115, 'Can delete Tipo de labor', 29, 'delete_tipolabor'),
(116, 'Can view Tipo de labor', 29, 'view_tipolabor'),
(117, 'Can add Programacion', 30, 'add_programacion'),
(118, 'Can change Programacion', 30, 'change_programacion'),
(119, 'Can delete Programacion', 30, 'delete_programacion'),
(120, 'Can view Programacion', 30, 'view_programacion'),
(121, 'Can add Ceco', 31, 'add_ceco'),
(122, 'Can change Ceco', 31, 'change_ceco'),
(123, 'Can delete Ceco', 31, 'delete_ceco'),
(124, 'Can view Ceco', 31, 'view_ceco');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ceco_ceco`
--

CREATE TABLE `ceco_ceco` (
  `idceco` int(11) NOT NULL,
  `ceco` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ceco_ceco`
--

INSERT INTO `ceco_ceco` (`idceco`, `ceco`, `estado`) VALUES
(1, 'RECURSOS HUMANOS', 0),
(2, 'RECURSOS HUMANOS', 0),
(3, 'RECURSOS HUMANOS', 0),
(4, 'RECURSOS HUMANOS', 0),
(5, 'RECURSOS HUMANOS', 1),
(6, 'LOGISTICA', 0),
(7, 'LOGISTICA', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_componente`
--

CREATE TABLE `componente_pieza_componente` (
  `idcomponente` int(11) NOT NULL,
  `componente` varchar(45) NOT NULL,
  `codcomponente` varchar(12) NOT NULL,
  `tiempovida` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL,
  `idsistema_id` int(11) NOT NULL,
  `frecuencia_man` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_pieza`
--

CREATE TABLE `componente_pieza_pieza` (
  `idpieza` int(11) NOT NULL,
  `pieza` varchar(45) NOT NULL,
  `codpieza` varchar(12) NOT NULL,
  `tiempoinstalacion` int(11) NOT NULL,
  `tiempovida` int(11) NOT NULL,
  `frecuenciaMP` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL,
  `idcomponente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componente_pieza_sistema`
--

CREATE TABLE `componente_pieza_sistema` (
  `idsistema` int(11) NOT NULL,
  `sistema` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-05-04 16:40:35.185370', '1', 'Asistente', 1, '[{\"added\": {}}]', 7, 2),
(2, '2024-05-04 16:40:42.500114', '2', 'Admin', 1, '[{\"added\": {}}]', 7, 2),
(3, '2024-05-04 16:40:48.297367', '3', 'Supervisor', 1, '[{\"added\": {}}]', 7, 2),
(4, '2024-05-04 16:40:58.800710', '4', 'Gerencia', 1, '[{\"added\": {}}]', 7, 2),
(5, '2024-05-04 16:43:50.209918', '1', 'Edwar Lopez 1', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Rol\"]}}]', 8, 2),
(6, '2024-05-04 16:44:04.139235', '2', 'Harold Quispe 2', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Rol\"]}}]', 8, 2),
(7, '2024-05-04 16:44:25.896251', '3', 'Josue Pisco 3', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Rol\"]}}]', 8, 2),
(8, '2024-05-04 16:44:46.465383', '4', 'Marco Huaman 4', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Rol\"]}}]', 8, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(31, 'ceco', 'ceco'),
(22, 'componente_pieza', 'componente'),
(24, 'componente_pieza', 'pieza'),
(23, 'componente_pieza', 'sistema'),
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
(25, 'operarios', 'solicitante'),
(26, 'operarios', 'tiposolicitante'),
(27, 'operarios', 'tractorista'),
(28, 'programacion_labor', 'detallelabor'),
(30, 'programacion_labor', 'programacion'),
(29, 'programacion_labor', 'tipolabor'),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-04 16:36:02.754380'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-05-04 16:36:02.810016'),
(3, 'auth', '0001_initial', '2024-05-04 16:36:03.017135'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-05-04 16:36:03.052202'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-05-04 16:36:03.055204'),
(6, 'auth', '0004_alter_user_username_opts', '2024-05-04 16:36:03.059892'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-05-04 16:36:03.062370'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-05-04 16:36:03.064350'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-05-04 16:36:03.067353'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-05-04 16:36:03.071354'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-05-04 16:36:03.074355'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-05-04 16:36:03.080354'),
(13, 'auth', '0011_update_proxy_permissions', '2024-05-04 16:36:03.084354'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-05-04 16:36:03.088097'),
(15, 'usuario', '0001_initial', '2024-05-04 16:36:03.316522'),
(16, 'admin', '0001_initial', '2024-05-04 16:36:03.395035'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-05-04 16:36:03.399036'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-04 16:36:03.405038'),
(19, 'ceco', '0001_initial', '2024-05-04 16:36:03.425612'),
(20, 'localizacion', '0001_initial', '2024-05-04 16:36:03.523986'),
(21, 'implemento', '0001_initial', '2024-05-04 16:36:03.660453'),
(22, 'componente_pieza', '0001_initial', '2024-05-04 16:36:03.790380'),
(23, 'implemento', '0002_initial', '2024-05-04 16:36:04.027145'),
(24, 'implemento', '0003_detimplementos_sistema', '2024-05-04 16:36:04.064928'),
(25, 'implemento', '0004_alter_detimplementos_options_and_more', '2024-05-04 16:36:04.384634'),
(26, 'componente_pieza', '0002_alter_componente_options_and_more', '2024-05-04 16:36:04.616384'),
(27, 'componente_pieza', '0003_componente_frecuencia_man', '2024-05-04 16:36:04.622383'),
(28, 'componente_pieza', '0004_pieza', '2024-05-04 16:36:04.676670'),
(29, 'fundo_cultivo', '0001_initial', '2024-05-04 16:36:04.905907'),
(30, 'fundo_cultivo', '0002_alter_variedad_variedad', '2024-05-04 16:36:05.033029'),
(31, 'implemento', '0005_remove_detimplementos_actualizado_en_and_more', '2024-05-04 16:36:05.354232'),
(32, 'implemento', '0006_remove_detimplementos_sistema_and_more', '2024-05-04 16:36:05.560438'),
(33, 'localizacion', '0002_alter_sede_sede', '2024-05-04 16:36:05.569481'),
(34, 'operarios', '0001_initial', '2024-05-04 16:36:05.645459'),
(35, 'operarios', '0002_initial', '2024-05-04 16:36:05.787200'),
(36, 'tractor', '0001_initial', '2024-05-04 16:36:05.898316'),
(37, 'programacion_labor', '0001_initial', '2024-05-04 16:36:06.103350'),
(38, 'programacion_labor', '0002_initial', '2024-05-04 16:36:06.194725'),
(39, 'programacion_labor', '0003_initial', '2024-05-04 16:36:06.354111'),
(40, 'sessions', '0001_initial', '2024-05-04 16:36:06.382120'),
(41, 'tractor', '0002_initial', '2024-05-04 16:36:06.523774'),
(42, 'tractor', '0003_remove_tractor_idcultivo_tractor_idfundo', '2024-05-04 16:36:06.760571'),
(43, 'tractor', '0003_alter_tipotractor_tipotractor', '2024-05-04 16:36:06.770571'),
(44, 'tractor', '0004_merge_20240424_0903', '2024-05-04 16:36:06.772571'),
(45, 'usuario', '0002_alter_persona_dni', '2024-05-04 16:36:06.775974'),
(46, 'implemento', '0007_alter_tipoimplemento_tipoimplemento', '2024-05-04 21:19:49.318785'),
(47, 'localizacion', '0003_alter_sede_sede', '2024-05-04 21:52:45.206607'),
(48, 'fundo_cultivo', '0003_alter_fundo_fundo', '2024-05-04 22:59:22.527933'),
(49, 'fundo_cultivo', '0004_alter_cultivo_cultivo_alter_lote_lote', '2024-05-04 23:36:10.680278'),
(50, 'ceco', '0002_alter_ceco_ceco', '2024-05-05 03:12:15.390516'),
(51, 'operarios', '0003_alter_tiposolicitante_tiposolicitante', '2024-05-05 03:23:14.488867'),
(52, 'usuario', '0003_alter_persona_dni', '2024-05-05 03:48:37.789634'),
(53, 'tractor', '0005_alter_tipotractor_tipotractor', '2024-05-05 04:35:14.268223'),
(54, 'tractor', '0006_alter_tractor_horauso', '2024-05-05 04:48:03.368428'),
(55, 'tractor', '0007_alter_tractor_nrotractor', '2024-05-05 05:03:52.020544');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1sr6nuuylviub6ejxclh5rhskb9sbiye', '.eJxVjEEOwiAQRe_C2pAyjEBduvcMZIBBqgaS0q6Md7dNutDte-__t_C0LsWvnWc_JXERKE6_LFB8ct1FelC9NxlbXeYpyD2Rh-3y1hK_rkf7d1Col22t8gA6WwiZTEZGZw07ZTVCtpETWDcGPegza8g4bERhcmFkQxHABBafL9-eOAw:1s4MiN:SbflsiYVKtEg9CvKk319i647ZszZ8ACKfnL54ejsHZk', '2024-05-21 15:26:47.851775'),
('3mhfvzsmo2ox8nxf2s4z13sx0y9txevs', '.eJxVjEEOwiAQRe_C2pDCAB1cuvcMZJghUjU0Ke3KeHdt0oVu_3vvv1Siba1p62VJk6izMur0u2XiR2k7kDu126x5busyZb0r-qBdX2cpz8vh_h1U6vVb84CGfRh9RmtCJEYbAcfiInjjxQ1sHRgphAAQ2COKA1c8mmwtSVbvD66DNrU:1s3ffM:4qUREXq_ni02zMB9jfQXiEiJh7zJKuk8Xm4wGSbwWXo', '2024-05-19 17:28:48.522397'),
('54j0iba50mzxz5t9ionvkpot0czqk6u4', '.eJxVjEEOwiAQRe_C2pDCAB1cuvcMZJghUjU0Ke3KeHdt0oVu_3vvv1Siba1p62VJk6izMur0u2XiR2k7kDu126x5busyZb0r-qBdX2cpz8vh_h1U6vVb84CGfRh9RmtCJEYbAcfiInjjxQ1sHRgphAAQ2COKA1c8mmwtSVbvD66DNrU:1s3UOZ:HT9NVI9FUq3vbe2TgJfKakDq2GY8rrEqQwwT06hjrCA', '2024-05-19 05:26:43.176160'),
('79wueeigulup7y4rxzvqf1e74rg2rh9v', '.eJxVjDEOwjAMRe-SGUWmiZvAyN4zRI5tSAGlUtNOiLtDpQ6w_vfef5lE61LS2nROo5iz6czhd8vED60bkDvV22R5qss8ZrspdqfNDpPo87K7fweFWvnWXk4Sub9GBIfKKkIeuEdQRojiIBNogMDqPABwBKHAyMfoEELH5v0B9ME35w:1s3W0H:lIvWCcimN6Ez8LbEhwkvT6yqQHp4PFdttkQsXDMpev4', '2024-05-19 07:09:45.042906'),
('a9fflwtjsb8cjn9lrh5x2zzq2szhl93w', '.eJxVjEEOgjAQRe_StWmYlg7WpXvOQGY6g6CmTSisjHdXEha6_e-9_zIDbes0bFWXYRZzMd6cfjem9NC8A7lTvhWbSl6Xme2u2INW2xfR5_Vw_w4mqtO3hhSgFQ84dq10DSRPjoNoh0xRzgmpQRwjIrAItI68OmLlFL36EJ15fwDkIzgl:1s4Mk5:uQnDOStX_uaRiLTnR8XlTKgJGt6BX4C_jy9T5P6FYrw', '2024-05-21 15:28:33.448556'),
('cxpebro3ci6wv3tyykn5zikfejzucj6y', '.eJxVjEEOwiAQRe_C2pDCAB1cuvcMZJghUjU0Ke3KeHdt0oVu_3vvv1Siba1p62VJk6izMur0u2XiR2k7kDu126x5busyZb0r-qBdX2cpz8vh_h1U6vVb84CGfRh9RmtCJEYbAcfiInjjxQ1sHRgphAAQ2COKA1c8mmwtSVbvD66DNrU:1s3JFM:Bow-GgHXoig7ZtS7KKyj5JdhZjB3Oj9LIMlKYTACdq4', '2024-05-18 17:32:28.023448'),
('d4abrfg4oqew17ifjtthchwvokg5duvc', '.eJxVjDEOwjAMRe-SGUWmiZvAyN4zRI5tSAGlUtNOiLtDpQ6w_vfef5lE61LS2nROo5iz6czhd8vED60bkDvV22R5qss8ZrspdqfNDpPo87K7fweFWvnWXk4Sub9GBIfKKkIeuEdQRojiIBNogMDqPABwBKHAyMfoEELH5v0B9ME35w:1s3VuM:WC9vN6qg6K8R_6U8KowpqI9Tdm1wBD8kORPN2SRoISY', '2024-05-19 07:03:38.633774'),
('jjsdl3k44sjzvazkt8ixbbbch3pgjiqe', '.eJxVjEEOgjAQRe_StWmYlg7WpXvOQGY6g6CmTSisjHdXEha6_e-9_zIDbes0bFWXYRZzMd6cfjem9NC8A7lTvhWbSl6Xme2u2INW2xfR5_Vw_w4mqtO3hhSgFQ84dq10DSRPjoNoh0xRzgmpQRwjIrAItI68OmLlFL36EJ15fwDkIzgl:1s3VSm:MKRw8-g17NmJ0wnXgV-UPVUSOZuShDTORMRtx5Pn5tA', '2024-05-19 06:35:08.127554'),
('m8vq7ulfqqkpp2eqbyc9jtdifkh20n0h', '.eJxVjEEOwiAQRe_C2pAyjEBduvcMZIBBqgaS0q6Md7dNutDte-__t_C0LsWvnWc_JXERKE6_LFB8ct1FelC9NxlbXeYpyD2Rh-3y1hK_rkf7d1Col22t8gA6WwiZTEZGZw07ZTVCtpETWDcGPegza8g4bERhcmFkQxHABBafL9-eOAw:1s3foA:D9zOcLBYc2QQRg6N9u2YfPBEc-vky9-6xlXFQlAIzK8', '2024-05-19 17:37:54.727774'),
('ri86t3i1hrlrbxsibjq0f84wfqilzxhn', '.eJxVjDEOwjAMRe-SGUWmiZvAyN4zRI5tSAGlUtNOiLtDpQ6w_vfef5lE61LS2nROo5iz6czhd8vED60bkDvV22R5qss8ZrspdqfNDpPo87K7fweFWvnWXk4Sub9GBIfKKkIeuEdQRojiIBNogMDqPABwBKHAyMfoEELH5v0B9ME35w:1s41dr:DbNnwBFXekgyGJFIpQnV3CobDFjbFhuUwPUgSANjQY8', '2024-05-20 16:56:43.829156');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_cultivo`
--

CREATE TABLE `fundo_cultivo_cultivo` (
  `idcultivo` int(11) NOT NULL,
  `cultivo` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fundo_cultivo_cultivo`
--

INSERT INTO `fundo_cultivo_cultivo` (`idcultivo`, `cultivo`, `estado`) VALUES
(1, 'ESPARRAGO', 1),
(2, 'VID', 1),
(3, 'ARANDANOS', 1),
(4, 'MANDARINA', 0),
(5, 'CEREZO', 1),
(6, 'CEREZO', 0),
(7, 'CEREZO', 0),
(8, 'CEREZO', 0),
(9, 'CEREZO', 0),
(10, 'CEREZO', 0),
(11, 'cerezo', 0),
(12, 'PALTO', 1),
(13, 'b', 0),
(14, 'PECANO', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_fundo`
--

CREATE TABLE `fundo_cultivo_fundo` (
  `idfundo` int(11) NOT NULL,
  `fundo` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idsede_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fundo_cultivo_fundo`
--

INSERT INTO `fundo_cultivo_fundo` (`idfundo`, `fundo`, `estado`, `idsede_id`) VALUES
(1, 'FORTUNA', 1, 1),
(2, 'SAN HILARION', 1, 3),
(3, 'PROYECTO VID', 1, 4),
(4, 'STA MARGARITA 1', 1, 4),
(5, 'a', 0, 4),
(6, 'a', 0, 4),
(7, 'a', 0, 4),
(8, 'a', 0, 1),
(9, 'LUREN', 1, 1),
(10, 'a', 0, 3),
(11, 'A', 0, 3);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fundo_cultivo_lote`
--

INSERT INTO `fundo_cultivo_lote` (`idlote`, `lote`, `estado`, `idfundo_id`, `idvariedad_id`) VALUES
(1, '1010', 1, 1, 5),
(2, '1020', 1, 3, 10),
(3, '1030', 1, 9, 2),
(4, '1040', 0, 2, 1),
(5, '1040', 1, 2, 1),
(6, '1050', 0, 2, 1),
(7, '1050', 0, 1, 3),
(8, '1050', 0, 2, 2),
(9, '1050', 1, 2, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fundo_cultivo_variedad`
--

CREATE TABLE `fundo_cultivo_variedad` (
  `idvariedad` int(11) NOT NULL,
  `variedad` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idcultivo_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fundo_cultivo_variedad`
--

INSERT INTO `fundo_cultivo_variedad` (`idvariedad`, `variedad`, `estado`, `idcultivo_id`) VALUES
(1, 'Hass', 1, 12),
(2, 'Fuerte', 1, 12),
(3, 'Zutano', 1, 12),
(4, 'Negras', 1, 2),
(5, 'Rojas', 1, 2),
(6, 'Rojas', 0, 2),
(7, 'Rojas', 0, 2),
(8, 'Verdes', 0, 2),
(9, 'Verde', 0, 2),
(10, 'Verde', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `implemento_detimplementos`
--

CREATE TABLE `implemento_detimplementos` (
  `iddetalleimplemento` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idimplemento_id` int(11) NOT NULL,
  `idcomponente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `implemento_implemento`
--

CREATE TABLE `implemento_implemento` (
  `idimplemento` int(11) NOT NULL,
  `implemento` varchar(45) NOT NULL,
  `tiempovida` int(11) NOT NULL,
  `horasdeuso` double NOT NULL,
  `codimplemento` varchar(12) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `estado_actividad` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` date NOT NULL,
  `idarea_id` int(11) NOT NULL,
  `idceco_id` int(11) NOT NULL,
  `idtipoimplemento_id` int(11) NOT NULL,
  `idusuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `implemento_implemento`
--

INSERT INTO `implemento_implemento` (`idimplemento`, `implemento`, `tiempovida`, `horasdeuso`, `codimplemento`, `estado`, `estado_actividad`, `creado_en`, `actualizado_en`, `idarea_id`, `idceco_id`, `idtipoimplemento_id`, `idusuario_id`) VALUES
(1, 'AZUFRADORA 1', 10000, 0, '1010', 1, 1, '2024-05-05 05:08:15.947373', '2024-05-05', 2, 7, 2, 2),
(2, 'AZUFRADORA 2', 10000, 10.8, '1020', 1, 1, '2024-05-05 05:09:05.534739', '2024-05-05', 2, 5, 2, 2),
(3, 'CHASKI 1', 35000, 0, '1030', 1, 1, '2024-05-05 05:10:48.858102', '2024-05-05', 4, 5, 4, 2),
(4, 'JACTO 1', 40000, 0, '1043', 1, 1, '2024-05-05 05:11:19.464817', '2024-05-05', 3, 5, 7, 3),
(5, 'ROTATIVA', 25000, 4.5, '9102', 1, 1, '2024-05-05 05:14:40.691075', '2024-05-05', 4, 5, 1, 3),
(6, 'ROTATIVA', 25000, 0, '9102', 0, 1, '2024-05-05 05:15:41.249161', '2024-05-05', 4, 5, 1, 3),
(7, 'ROTATIVA 2', 25000, 0, '9106', 0, 1, '2024-05-05 05:23:14.761560', '2024-05-05', 4, 5, 1, 3),
(8, 'ROTATIVA 1', 25000, 0, '9104', 0, 1, '2024-05-05 05:23:25.211882', '2024-05-05', 4, 5, 1, 3),
(9, 'ROTATIVA 3', 25000, 0, '9109', 0, 1, '2024-05-05 05:27:13.467179', '2024-05-05', 4, 5, 1, 3),
(10, 'ROTATIVA 1', 25000, 0, '9102', 0, 1, '2024-05-05 05:31:20.134995', '2024-05-05', 4, 5, 1, 3),
(11, 'ROTATIVA 1', 25000, 0, '9102', 0, 1, '2024-05-05 05:31:34.342052', '2024-05-05', 4, 5, 1, 3),
(12, 'ROTATIVA 1', 25000, 0, '9102', 0, 1, '2024-05-05 05:31:51.650308', '2024-05-05', 4, 5, 1, 3),
(13, 'ROTATIVA 4', 25000, 0, '9109', 0, 1, '2024-05-05 05:32:34.511455', '2024-05-05', 4, 5, 1, 3),
(14, 'ROTATIVA 2', 25000, 9, '9102', 1, 1, '2024-05-05 05:34:05.417712', '2024-05-05', 4, 5, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `implemento_tipoimplemento`
--

CREATE TABLE `implemento_tipoimplemento` (
  `idtipoimplemento` int(11) NOT NULL,
  `tipoimplemento` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `implemento_tipoimplemento`
--

INSERT INTO `implemento_tipoimplemento` (`idtipoimplemento`, `tipoimplemento`, `estado`) VALUES
(1, 'ROTATIVA', 1),
(2, 'AZUFRADORA', 1),
(3, 'ROTATIVA', 0),
(4, 'CHASKI VID', 1),
(5, 'A', 0),
(6, 'A', 0),
(7, 'JACTO', 1),
(8, 'ROTATIVA', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizacion_area`
--

CREATE TABLE `localizacion_area` (
  `idarea` int(11) NOT NULL,
  `area` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idbase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `localizacion_area`
--

INSERT INTO `localizacion_area` (`idarea`, `area`, `estado`, `idbase_id`) VALUES
(1, 'MECANICA', 0, 1),
(2, 'ELECTRICIDAD', 1, 2),
(3, 'SOLDADURA', 1, 3),
(4, 'MECANICA', 1, 1),
(5, 'LLANTEROS', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizacion_base`
--

CREATE TABLE `localizacion_base` (
  `idbase` int(11) NOT NULL,
  `base` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `idsede_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `localizacion_base`
--

INSERT INTO `localizacion_base` (`idbase`, `base`, `estado`, `idsede_id`) VALUES
(1, 'LOS CASTILLAS', 1, 1),
(2, 'RAMON YAN', 1, 3),
(3, 'VID', 1, 1),
(4, 'B', 0, 3),
(5, 'b', 0, 3),
(6, 'NIGGAS', 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizacion_sede`
--

CREATE TABLE `localizacion_sede` (
  `idsede` int(11) NOT NULL,
  `sede` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `localizacion_sede`
--

INSERT INTO `localizacion_sede` (`idsede`, `sede`, `estado`) VALUES
(1, 'SEDE CHINCHA', 1),
(2, 'SEDE ICA', 0),
(3, 'SEDE ICA', 1),
(4, 'SEDE LIMA', 1),
(5, 'SEDE ICA', 0),
(6, 'a', 0),
(7, 'a', 0);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operarios_solicitante`
--

INSERT INTO `operarios_solicitante` (`idsolicitante`, `estado`, `estado_actividad`, `creado_en`, `actualizado_en`, `idpersona_id`, `idtiposolicitante_id`) VALUES
(1, 1, 1, '2024-05-05 03:55:11.064307', '2024-05-04', 1, 4),
(2, 1, 1, '2024-05-05 03:55:50.481918', '2024-05-04', 3, 4),
(3, 1, 1, '2024-05-05 04:03:53.901051', '2024-05-04', 4, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operarios_tiposolicitante`
--

CREATE TABLE `operarios_tiposolicitante` (
  `idtiposolicitante` int(11) NOT NULL,
  `tiposolicitante` varchar(45) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operarios_tiposolicitante`
--

INSERT INTO `operarios_tiposolicitante` (`idtiposolicitante`, `tiposolicitante`, `estado`) VALUES
(1, 'JEFE DE FUNDO', 0),
(2, 'JEFE DE FUNDO', 0),
(3, 'JEFE DE SANIDAD', 1),
(4, 'JEDE DE FUNDO', 1),
(5, 'a', 0),
(6, 'A', 0),
(7, 'a', 0);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operarios_tractorista`
--

INSERT INTO `operarios_tractorista` (`idtractorista`, `estado`, `estado_actividad`, `creado_en`, `actualizado_en`, `idpersona_id`, `idusuario_id`) VALUES
(1, 1, 1, '2024-05-05 04:16:41.085130', '2024-05-04', 5, 2),
(2, 1, 1, '2024-05-05 04:17:15.711904', '2024-05-04', 6, 3),
(3, 1, 1, '2024-05-05 04:19:27.445317', '2024-05-04', 7, 2),
(4, 1, 1, '2024-05-05 04:20:07.961063', '2024-05-04', 8, 3);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `programacion_labor_detallelabor`
--

INSERT INTO `programacion_labor_detallelabor` (`iddetlabor`, `horadeuso`, `estado`, `idimplemento_id`, `idprogramacion_id`) VALUES
(1, 10, 1, 1, 1),
(2, 8, 1, 2, 2),
(3, 12, 1, 4, 3),
(4, 10, 1, 1, 4),
(5, 10, 1, 2, 5),
(6, 5, 1, 3, 6),
(7, 8, 1, 4, 7),
(8, 4, 1, 5, 8),
(9, 10, 1, 2, 9),
(10, 10, 1, 4, 10),
(11, 15, 1, 14, 11),
(12, 25, 1, 5, 12),
(13, 5, 1, 14, 13),
(14, 10, 1, 14, 14);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `programacion_labor_programacion`
--

INSERT INTO `programacion_labor_programacion` (`idprogramacion`, `fechahora`, `turno`, `estado`, `idlote_id`, `idsolicitante_id`, `idtipolabor_id`, `idtractor_id`, `idtractorista_id`, `idusuario_id`) VALUES
(1, '2024-05-05', 'M', 0, 1, 1, 2, 2, 1, 2),
(2, '2024-05-05', 'T', 0, 2, 2, 3, 7, 4, 2),
(3, '2024-05-05', 'M', 0, 5, 1, 2, 6, 2, 2),
(4, '2024-05-05', 'M', 0, 5, 2, 3, 8, 1, 2),
(5, '2024-05-06', 'T', 0, 9, 2, 5, 3, 3, 2),
(6, '2024-05-05', 'M', 0, 1, 1, 1, 2, 2, 2),
(7, '2024-05-05', 'M', 0, 1, 1, 2, 6, 4, 3),
(8, '2024-05-06', 'M', 0, 2, 2, 3, 3, 4, 3),
(9, '2024-05-06', 'T', 0, 9, 3, 2, 7, 1, 3),
(10, '2024-05-05', 'M', 0, 1, 2, 3, 6, 2, 3),
(11, '2024-05-07', 'M', 0, 1, 1, 3, 8, 4, 3),
(12, '2024-05-07', 'M', 0, 1, 2, 3, 7, 4, 3),
(13, '2024-05-08', 'N', 0, 5, 3, 3, 6, 1, 3),
(14, '2024-05-08', 'T', 0, 1, 3, 4, 8, 4, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programacion_labor_tipolabor`
--

CREATE TABLE `programacion_labor_tipolabor` (
  `idtipolabor` int(11) NOT NULL,
  `tipolabor` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `programacion_labor_tipolabor`
--

INSERT INTO `programacion_labor_tipolabor` (`idtipolabor`, `tipolabor`, `estado`) VALUES
(1, 'DESBROCE', 1),
(2, 'APLICACIÓN', 1),
(3, 'COSECHA', 1),
(4, 'SUBSULADO', 1),
(5, 'DESQUILLER', 1);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tractor_reportetractor`
--

INSERT INTO `tractor_reportetractor` (`idreportetractor`, `horometroinicial`, `horometrofinal`, `correlativo`, `estado`, `idprogramacion_id`, `idusuario_id`) VALUES
(1, 100, 110, 123123, 1, 1, 4),
(2, 100, 108, 4124, 1, 2, 4),
(3, 100, 112, 91421, 1, 3, 4),
(4, 100, 110, 123891, 1, 4, 4),
(5, 100, 110, 19824, 1, 5, 4),
(6, 110, 115, 124124, 1, 6, 4),
(7, 112, 120, 12812, 1, 7, 4),
(8, 120, 130, 213812, 1, 10, 4),
(9, 108, 120, 87123, 1, 9, 4),
(10, 110, 115, 143124, 1, 8, 4),
(11, 110, 115, 12412, 1, 11, 4),
(12, 120, 125, 14124, 1, 12, 4),
(13, 130, 135, 1041, 1, 13, 4),
(14, 115, 125, 85124, 1, 14, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tractor_tipotractor`
--

CREATE TABLE `tractor_tipotractor` (
  `idtipotractor` int(11) NOT NULL,
  `TipoTractor` varchar(100) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tractor_tipotractor`
--

INSERT INTO `tractor_tipotractor` (`idtipotractor`, `TipoTractor`, `estado`) VALUES
(1, 'VIÑATERO', 1),
(2, 'DOBLE', 1),
(3, 'SIMPLE', 0),
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
  `idtipotractor_id` int(11) NOT NULL,
  `idusuario_id` bigint(20) DEFAULT NULL,
  `idfundo_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tractor_tractor`
--

INSERT INTO `tractor_tractor` (`idtractor`, `nrotractor`, `horainicial`, `horauso`, `estado`, `estado_actividad`, `idtipotractor_id`, `idusuario_id`, `idfundo_id`) VALUES
(1, 'Viñatero 1', 100, 0, 1, 1, 1, 2, 1),
(2, 'VIÑATERO 2', 115, 15, 1, 1, 1, 2, 9),
(3, 'VIÑATERO 3', 115, 15, 1, 1, 1, 2, 4),
(4, 'DOBLE 1', 100, 0, 1, 1, 2, 2, 3),
(5, 'DOBLE 2', 100, 0, 1, 1, 2, 2, 2),
(6, 'SIMPLE 1', 135, 35, 1, 1, 4, 3, 2),
(7, 'VIÑATERO 4', 125, 25, 1, 1, 1, 3, 2),
(8, 'VIÑATERO 10', 125, 25, 1, 1, 1, 3, 2);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario_persona`
--

INSERT INTO `usuario_persona` (`idpersona`, `nombres`, `apellidos`, `dni`, `codigo`, `estado`, `creado_en`, `actualizado_en`) VALUES
(1, 'SAMUEL', 'LOPEZ', '72472737', '1000', 1, '2024-05-05 03:55:11.061310', '2024-05-04'),
(2, 'JUAN', 'HUMAN', '91784819', '1001', 1, '2024-05-05 03:55:25.099309', '2024-05-04'),
(3, 'JUAN', 'PEREZ', '18471892', '1002', 1, '2024-05-05 03:55:50.470900', '2024-05-04'),
(4, 'OLVA', 'GOMEZ', '91487912', '1003', 1, '2024-05-05 04:03:53.887869', '2024-05-04'),
(5, 'Samanta', 'Pisco', '19479182', '1004', 1, '2024-05-05 04:16:41.071083', '2024-05-04'),
(6, 'JULIO', 'SIERRA', '19458192', '1005', 1, '2024-05-05 04:17:15.701726', '2024-05-04'),
(7, 'Mateo', 'Aguirre', '91479187', '1006', 1, '2024-05-05 04:19:27.439315', '2024-05-04'),
(8, 'Jorge', 'Luna', '14987129', '1007', 1, '2024-05-05 04:20:07.951834', '2024-05-04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_rol`
--

CREATE TABLE `usuario_rol` (
  `idrol` int(11) NOT NULL,
  `rol` varchar(30) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario_rol`
--

INSERT INTO `usuario_rol` (`idrol`, `rol`, `estado`) VALUES
(1, 'Asistente', 1),
(2, 'Admin', 1),
(3, 'Supervisor', 1),
(4, 'Gerencia', 1);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario_usuario`
--

INSERT INTO `usuario_usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `idrol_id`) VALUES
(1, 'pbkdf2_sha256$600000$htsJBpYSbHHVW6srWRhhos$FBEBGispty2dzCY6zpdtLWylT5txuWCZeKgrFl00bCs=', '2024-05-06 16:51:35.400243', 1, 'admin', 'Edwar', 'Lopez', 'admin@gmail.copm', 1, 1, '2024-05-04 16:37:32.000000', 2),
(2, 'pbkdf2_sha256$600000$FWTJloJLbGRGhsNnE6Z0rJ$rh8SxMQWMw5HL4HgSC0XICOYibdpWrJfoO1nFeZqo7g=', '2024-05-06 16:56:43.821787', 1, 'harold', 'Harold', 'Quispe', 'harold@gmail.com', 1, 1, '2024-05-04 16:38:34.000000', 3),
(3, 'pbkdf2_sha256$600000$BSX8Sq4NLEtkaQsqAhYrqE$VVQjM+W7QIJK4lMjTCjAoO9iP2t/YW4CtIPS5hgXIEI=', '2024-05-07 15:28:33.446047', 1, 'josue', 'Josue', 'Pisco', 'josue@gmail.com', 1, 1, '2024-05-04 16:38:50.000000', 3),
(4, 'pbkdf2_sha256$600000$9Qhkr7W7EfhE3BZntKLrqC$DVubQceS1lcQPhLJJQJty72HZlqMdEpxCBrg5XGCjDI=', '2024-05-07 15:26:47.848942', 1, 'asistente', 'Marco', 'Huaman', 'asistente@gmail.com', 1, 1, '2024-05-04 16:39:34.000000', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_usuario_groups`
--

CREATE TABLE `usuario_usuario_groups` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_usuario_user_permissions`
--

CREATE TABLE `usuario_usuario_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  ADD KEY `componente_pieza_com_idsistema_id_1ae99d54_fk_component` (`idsistema_id`);

--
-- Indices de la tabla `componente_pieza_pieza`
--
ALTER TABLE `componente_pieza_pieza`
  ADD PRIMARY KEY (`idpieza`),
  ADD KEY `componente_pieza_pie_idcomponente_id_ec1330e0_fk_component` (`idcomponente_id`);

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
  ADD KEY `implemento_detimplem_idimplemento_id_4fa089b3_fk_implement` (`idimplemento_id`),
  ADD KEY `implemento_detimplem_idcomponente_id_43784524_fk_component` (`idcomponente_id`);

--
-- Indices de la tabla `implemento_implemento`
--
ALTER TABLE `implemento_implemento`
  ADD PRIMARY KEY (`idimplemento`),
  ADD KEY `implemento_implement_idarea_id_8577a5ca_fk_localizac` (`idarea_id`),
  ADD KEY `implemento_implemento_idceco_id_2c850f10_fk_ceco_ceco_idceco` (`idceco_id`),
  ADD KEY `implemento_implement_idtipoimplemento_id_5fd9fe6e_fk_implement` (`idtipoimplemento_id`),
  ADD KEY `implemento_implement_idusuario_id_38219cf9_fk_usuario_u` (`idusuario_id`);

--
-- Indices de la tabla `implemento_tipoimplemento`
--
ALTER TABLE `implemento_tipoimplemento`
  ADD PRIMARY KEY (`idtipoimplemento`);

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
  ADD KEY `tractor_tractor_idtipotractor_id_e0cf7d46_fk_tractor_t` (`idtipotractor_id`),
  ADD KEY `tractor_tractor_idusuario_id_6e5caf82_fk_usuario_usuario_id` (`idusuario_id`),
  ADD KEY `tractor_tractor_idfundo_id_7c9f50e5_fk_fundo_cul` (`idfundo_id`);

--
-- Indices de la tabla `usuario_persona`
--
ALTER TABLE `usuario_persona`
  ADD PRIMARY KEY (`idpersona`),
  ADD UNIQUE KEY `usuario_persona_dni_16d67f30_uniq` (`dni`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=125;

--
-- AUTO_INCREMENT de la tabla `ceco_ceco`
--
ALTER TABLE `ceco_ceco`
  MODIFY `idceco` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_componente`
--
ALTER TABLE `componente_pieza_componente`
  MODIFY `idcomponente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_pieza`
--
ALTER TABLE `componente_pieza_pieza`
  MODIFY `idpieza` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `componente_pieza_sistema`
--
ALTER TABLE `componente_pieza_sistema`
  MODIFY `idsistema` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_cultivo`
--
ALTER TABLE `fundo_cultivo_cultivo`
  MODIFY `idcultivo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_fundo`
--
ALTER TABLE `fundo_cultivo_fundo`
  MODIFY `idfundo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_lote`
--
ALTER TABLE `fundo_cultivo_lote`
  MODIFY `idlote` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `fundo_cultivo_variedad`
--
ALTER TABLE `fundo_cultivo_variedad`
  MODIFY `idvariedad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `implemento_detimplementos`
--
ALTER TABLE `implemento_detimplementos`
  MODIFY `iddetalleimplemento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `implemento_implemento`
--
ALTER TABLE `implemento_implemento`
  MODIFY `idimplemento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `implemento_tipoimplemento`
--
ALTER TABLE `implemento_tipoimplemento`
  MODIFY `idtipoimplemento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `localizacion_area`
--
ALTER TABLE `localizacion_area`
  MODIFY `idarea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `localizacion_base`
--
ALTER TABLE `localizacion_base`
  MODIFY `idbase` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `localizacion_sede`
--
ALTER TABLE `localizacion_sede`
  MODIFY `idsede` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `operarios_solicitante`
--
ALTER TABLE `operarios_solicitante`
  MODIFY `idsolicitante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `operarios_tiposolicitante`
--
ALTER TABLE `operarios_tiposolicitante`
  MODIFY `idtiposolicitante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `operarios_tractorista`
--
ALTER TABLE `operarios_tractorista`
  MODIFY `idtractorista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `programacion_labor_detallelabor`
--
ALTER TABLE `programacion_labor_detallelabor`
  MODIFY `iddetlabor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `programacion_labor_programacion`
--
ALTER TABLE `programacion_labor_programacion`
  MODIFY `idprogramacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `programacion_labor_tipolabor`
--
ALTER TABLE `programacion_labor_tipolabor`
  MODIFY `idtipolabor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tractor_reportetractor`
--
ALTER TABLE `tractor_reportetractor`
  MODIFY `idreportetractor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `tractor_tipotractor`
--
ALTER TABLE `tractor_tipotractor`
  MODIFY `idtipotractor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tractor_tractor`
--
ALTER TABLE `tractor_tractor`
  MODIFY `idtractor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuario_persona`
--
ALTER TABLE `usuario_persona`
  MODIFY `idpersona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuario_rol`
--
ALTER TABLE `usuario_rol`
  MODIFY `idrol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
-- Filtros para la tabla `componente_pieza_pieza`
--
ALTER TABLE `componente_pieza_pieza`
  ADD CONSTRAINT `componente_pieza_pie_idcomponente_id_ec1330e0_fk_component` FOREIGN KEY (`idcomponente_id`) REFERENCES `componente_pieza_componente` (`idcomponente`);

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
  ADD CONSTRAINT `implemento_detimplem_idcomponente_id_43784524_fk_component` FOREIGN KEY (`idcomponente_id`) REFERENCES `componente_pieza_componente` (`idcomponente`),
  ADD CONSTRAINT `implemento_detimplem_idimplemento_id_4fa089b3_fk_implement` FOREIGN KEY (`idimplemento_id`) REFERENCES `implemento_implemento` (`idimplemento`);

--
-- Filtros para la tabla `implemento_implemento`
--
ALTER TABLE `implemento_implemento`
  ADD CONSTRAINT `implemento_implement_idarea_id_8577a5ca_fk_localizac` FOREIGN KEY (`idarea_id`) REFERENCES `localizacion_area` (`idarea`),
  ADD CONSTRAINT `implemento_implement_idtipoimplemento_id_5fd9fe6e_fk_implement` FOREIGN KEY (`idtipoimplemento_id`) REFERENCES `implemento_tipoimplemento` (`idtipoimplemento`),
  ADD CONSTRAINT `implemento_implement_idusuario_id_38219cf9_fk_usuario_u` FOREIGN KEY (`idusuario_id`) REFERENCES `usuario_usuario` (`id`),
  ADD CONSTRAINT `implemento_implemento_idceco_id_2c850f10_fk_ceco_ceco_idceco` FOREIGN KEY (`idceco_id`) REFERENCES `ceco_ceco` (`idceco`);

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
