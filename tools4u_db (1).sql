-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 25, 2025 at 01:00 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tools4u_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_category`
--

DROP TABLE IF EXISTS `adminapp_tbl_category`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(40) NOT NULL,
  `category_image` varchar(100) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_category`
--

INSERT INTO `adminapp_tbl_category` (`category_id`, `category_name`, `category_image`) VALUES
(3, 'Motorized', 'motorized_GBnS96O.webp'),
(4, 'Non Motorized', 'toolset.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

DROP TABLE IF EXISTS `adminapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_district` (
  `district_id` int(11) NOT NULL AUTO_INCREMENT,
  `district_name` varchar(40) NOT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`district_id`, `district_name`) VALUES
(1, 'Eranakulam'),
(2, 'Thiruvananthapuram'),
(3, 'Kollam'),
(4, 'Pathanamthitta'),
(5, 'Alappuzha'),
(6, 'Kottayam'),
(7, 'Idukki'),
(8, 'Thrissur'),
(9, 'Palakkad'),
(10, 'Malappuram'),
(11, 'Kozhikode'),
(12, 'Wayanad'),
(13, 'Kannur'),
(14, 'Kasaragod');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

DROP TABLE IF EXISTS `adminapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `location_name` varchar(40) NOT NULL,
  `district_id_id` int(11) NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `AdminApp_tbl_location_district_id_id_006b89d6` (`district_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`location_id`, `location_name`, `district_id_id`) VALUES
(1, 'Kakkanad', 1),
(6, 'Thodupuzha', 7),
(5, 'Muvatupuzha', 7);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_subcategory`
--

DROP TABLE IF EXISTS `adminapp_tbl_subcategory`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_name` varchar(40) NOT NULL,
  `subcategory_image` varchar(100) NOT NULL,
  `category_id_id` int(11) NOT NULL,
  PRIMARY KEY (`subcategory_id`),
  KEY `AdminApp_tbl_subcategory_category_id_id_32bd919d` (`category_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_subcategory`
--

INSERT INTO `adminapp_tbl_subcategory` (`subcategory_id`, `subcategory_name`, `subcategory_image`, `category_id_id`) VALUES
(4, 'Cutting', 'Electric_Power_Tools_Zy6RnID.jpg', 3),
(5, 'Building', 'motorized_Tbc7Kwi.webp', 3),
(6, 'Cutting', 'toolset_CT243ha.jpg', 4),
(7, 'Building', 'nonmotorized_iINABBa.webp', 4),
(8, 'Electrical', 'conductivity_chech_tool.jpg', 4);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
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
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_login', 7, 'add_tbl_login'),
(26, 'Can change tbl_login', 7, 'change_tbl_login'),
(27, 'Can delete tbl_login', 7, 'delete_tbl_login'),
(28, 'Can view tbl_login', 7, 'view_tbl_login'),
(29, 'Can add tbl_district', 8, 'add_tbl_district'),
(30, 'Can change tbl_district', 8, 'change_tbl_district'),
(31, 'Can delete tbl_district', 8, 'delete_tbl_district'),
(32, 'Can view tbl_district', 8, 'view_tbl_district'),
(33, 'Can add tbl_location', 9, 'add_tbl_location'),
(34, 'Can change tbl_location', 9, 'change_tbl_location'),
(35, 'Can delete tbl_location', 9, 'delete_tbl_location'),
(36, 'Can view tbl_location', 9, 'view_tbl_location'),
(37, 'Can add tbl_category', 10, 'add_tbl_category'),
(38, 'Can change tbl_category', 10, 'change_tbl_category'),
(39, 'Can delete tbl_category', 10, 'delete_tbl_category'),
(40, 'Can view tbl_category', 10, 'view_tbl_category'),
(41, 'Can add tbl_subcategory', 11, 'add_tbl_subcategory'),
(42, 'Can change tbl_subcategory', 11, 'change_tbl_subcategory'),
(43, 'Can delete tbl_subcategory', 11, 'delete_tbl_subcategory'),
(44, 'Can view tbl_subcategory', 11, 'view_tbl_subcategory'),
(45, 'Can add tbl_user', 12, 'add_tbl_user'),
(46, 'Can change tbl_user', 12, 'change_tbl_user'),
(47, 'Can delete tbl_user', 12, 'delete_tbl_user'),
(48, 'Can view tbl_user', 12, 'view_tbl_user'),
(49, 'Can add tbl_seller', 13, 'add_tbl_seller'),
(50, 'Can change tbl_seller', 13, 'change_tbl_seller'),
(51, 'Can delete tbl_seller', 13, 'delete_tbl_seller'),
(52, 'Can view tbl_seller', 13, 'view_tbl_seller'),
(53, 'Can add tbl_tool', 14, 'add_tbl_tool'),
(54, 'Can change tbl_tool', 14, 'change_tbl_tool'),
(55, 'Can delete tbl_tool', 14, 'delete_tbl_tool'),
(56, 'Can view tbl_tool', 14, 'view_tbl_tool'),
(57, 'Can add tbl_rentrequest', 15, 'add_tbl_rentrequest'),
(58, 'Can change tbl_rentrequest', 15, 'change_tbl_rentrequest'),
(59, 'Can delete tbl_rentrequest', 15, 'delete_tbl_rentrequest'),
(60, 'Can view tbl_rentrequest', 15, 'view_tbl_rentrequest'),
(61, 'Can add tbl_purchaserequest', 16, 'add_tbl_purchaserequest'),
(62, 'Can change tbl_purchaserequest', 16, 'change_tbl_purchaserequest'),
(63, 'Can delete tbl_purchaserequest', 16, 'delete_tbl_purchaserequest'),
(64, 'Can view tbl_purchaserequest', 16, 'view_tbl_purchaserequest'),
(65, 'Can add tbl_payment', 17, 'add_tbl_payment'),
(66, 'Can change tbl_payment', 17, 'change_tbl_payment'),
(67, 'Can delete tbl_payment', 17, 'delete_tbl_payment'),
(68, 'Can view tbl_payment', 17, 'view_tbl_payment'),
(69, 'Can add tbl_purchasepayment', 18, 'add_tbl_purchasepayment'),
(70, 'Can change tbl_purchasepayment', 18, 'change_tbl_purchasepayment'),
(71, 'Can delete tbl_purchasepayment', 18, 'delete_tbl_purchasepayment'),
(72, 'Can view tbl_purchasepayment', 18, 'view_tbl_purchasepayment'),
(73, 'Can add tbl_rentepayment', 19, 'add_tbl_rentepayment'),
(74, 'Can change tbl_rentepayment', 19, 'change_tbl_rentepayment'),
(75, 'Can delete tbl_rentepayment', 19, 'delete_tbl_rentepayment'),
(76, 'Can view tbl_rentepayment', 19, 'view_tbl_rentepayment'),
(77, 'Can add tbl_rentpayment', 19, 'add_tbl_rentpayment'),
(78, 'Can change tbl_rentpayment', 19, 'change_tbl_rentpayment'),
(79, 'Can delete tbl_rentpayment', 19, 'delete_tbl_rentpayment'),
(80, 'Can view tbl_rentpayment', 19, 'view_tbl_rentpayment'),
(81, 'Can add timetable entry', 20, 'add_timetableentry'),
(82, 'Can change timetable entry', 20, 'change_timetableentry'),
(83, 'Can delete timetable entry', 20, 'delete_timetableentry'),
(84, 'Can view timetable entry', 20, 'view_timetableentry'),
(85, 'Can add class group', 21, 'add_classgroup'),
(86, 'Can change class group', 21, 'change_classgroup'),
(87, 'Can delete class group', 21, 'delete_classgroup'),
(88, 'Can view class group', 21, 'view_classgroup'),
(89, 'Can add time slot', 22, 'add_timeslot'),
(90, 'Can change time slot', 22, 'change_timeslot'),
(91, 'Can delete time slot', 22, 'delete_timeslot'),
(92, 'Can view time slot', 22, 'view_timeslot'),
(93, 'Can add teacher', 23, 'add_teacher'),
(94, 'Can change teacher', 23, 'change_teacher'),
(95, 'Can delete teacher', 23, 'delete_teacher'),
(96, 'Can view teacher', 23, 'view_teacher'),
(97, 'Can add subject', 24, 'add_subject'),
(98, 'Can change subject', 24, 'change_subject'),
(99, 'Can delete subject', 24, 'delete_subject'),
(100, 'Can view subject', 24, 'view_subject');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'GuestApp', 'tbl_login'),
(8, 'AdminApp', 'tbl_district'),
(9, 'AdminApp', 'tbl_location'),
(10, 'AdminApp', 'tbl_category'),
(11, 'AdminApp', 'tbl_subcategory'),
(12, 'GuestApp', 'tbl_user'),
(13, 'GuestApp', 'tbl_seller'),
(14, 'SellerApp', 'tbl_tool'),
(15, 'UserApp', 'tbl_rentrequest'),
(16, 'UserApp', 'tbl_purchaserequest'),
(17, 'UserApp', 'tbl_payment'),
(18, 'UserApp', 'tbl_purchasepayment'),
(19, 'UserApp', 'tbl_rentpayment'),
(20, 'GuestApp', 'timetableentry'),
(21, 'GuestApp', 'classgroup'),
(22, 'GuestApp', 'timeslot'),
(23, 'GuestApp', 'teacher'),
(24, 'GuestApp', 'subject');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'GuestApp', '0001_initial', '2025-01-08 08:56:17.935949'),
(2, 'contenttypes', '0001_initial', '2025-01-08 08:56:17.972134'),
(3, 'auth', '0001_initial', '2025-01-08 08:56:18.198659'),
(4, 'admin', '0001_initial', '2025-01-08 08:56:18.259424'),
(5, 'admin', '0002_logentry_remove_auto_add', '2025-01-08 08:56:18.272966'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-08 08:56:18.284160'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-01-08 08:56:18.329800'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-01-08 08:56:18.355538'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-01-08 08:56:18.381093'),
(10, 'auth', '0004_alter_user_username_opts', '2025-01-08 08:56:18.395090'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-01-08 08:56:18.419419'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-01-08 08:56:18.425587'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-01-08 08:56:18.470341'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-01-08 08:56:18.493969'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-01-08 08:56:18.516713'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-01-08 08:56:18.539621'),
(17, 'auth', '0011_update_proxy_permissions', '2025-01-08 08:56:18.553019'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-01-08 08:56:18.576267'),
(19, 'sessions', '0001_initial', '2025-01-08 08:56:18.599614'),
(20, 'AdminApp', '0001_initial', '2025-01-08 09:45:15.398903'),
(21, 'AdminApp', '0002_tbl_location', '2025-01-13 04:43:13.136748'),
(22, 'AdminApp', '0003_tbl_category', '2025-01-13 05:54:33.983600'),
(23, 'AdminApp', '0004_tbl_subcategory', '2025-01-15 04:30:09.835884'),
(24, 'GuestApp', '0002_tbl_user', '2025-01-21 06:42:52.485812'),
(25, 'GuestApp', '0003_alter_tbl_user_user_email', '2025-01-22 07:07:34.175757'),
(26, 'GuestApp', '0004_tbl_seller', '2025-01-23 08:23:45.389077'),
(27, 'SellerApp', '0001_initial', '2025-01-24 05:21:26.558887'),
(28, 'SellerApp', '0002_remove_tbl_tool_tool_category_and_more', '2025-01-24 06:48:51.578361'),
(29, 'UserApp', '0001_initial', '2025-02-11 06:19:15.418814'),
(30, 'UserApp', '0002_alter_tbl_rentrequest_request_remark_and_more', '2025-02-12 04:26:59.880703'),
(31, 'UserApp', '0003_remove_tbl_purchaserequest_purchase_remark', '2025-02-18 08:38:45.731506'),
(32, 'UserApp', '0004_tbl_payment', '2025-02-18 08:48:28.459170'),
(33, 'UserApp', '0005_tbl_purchasepayment_delete_tbl_payment', '2025-02-18 09:13:47.959067'),
(34, 'UserApp', '0006_tbl_rentepayment', '2025-02-27 10:11:01.528719'),
(35, 'UserApp', '0007_rename_tbl_rentepayment_tbl_rentpayment', '2025-02-27 10:11:38.308113'),
(36, 'UserApp', '0008_alter_tbl_rentpayment_rpayment_status', '2025-02-27 10:48:13.409095'),
(37, 'UserApp', '0009_alter_tbl_rentpayment_rpayment_status', '2025-02-27 10:50:01.339948'),
(38, 'GuestApp', '0005_classgroup_teacher_timeslot_subject_timetableentry', '2025-05-23 05:33:50.265393');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('y7xlnria9iqy88j4cksltcwtn05fxskm', 'eyJsb2dpbklkIjoxfQ:1tVShk:qV8uDJJwtK1h_W7MaqzkRkidcRGnqD1irg4b9V4aHy0', '2025-01-22 09:50:24.762941'),
('a0rrpdvl2nbpavcn8iff2ujm2j05f0z7', 'eyJsb2dpbklkIjoxfQ:1tXEFC:WFvMtTYgCKn4t157lAAuqwKCx8AQL8kazPhzG3AypxM', '2025-01-27 06:48:14.862864'),
('xx1eshe0d8utxndmn1sposvrbt0wdg5o', 'eyJsb2dpbklkIjoxfQ:1tXwZy:tk-G6nJJ-gcqLnGRPAsB1sWOJ-hy_uLiaadUdig6aJs', '2025-01-29 06:08:38.734550'),
('0o97rq10cp0qjbbxdzljr295pnxe4682', 'eyJsb2dpbklkIjoxfQ:1tYL59:wg_fWfwjDo2suJNgXk-udDyKiPOn2VtKbPfr7_A7l-o', '2025-01-30 08:18:27.741995'),
('z9szmi7jun1rm6qm4sogo15p6m5xrfoq', 'eyJsb2dpbklkIjoyfQ:1tZnDO:6RVth15nFWoBerSKZXtN37laY1oOEPc8jGNAgVSzC1A', '2025-02-03 08:32:58.407372'),
('835ughkjhqv1booejmzpqsnuxy15wqa7', 'eyJsb2dpbklkIjoyfQ:1ta6qr:T4xwgwctAqFXlb6ruXinN_x1mf4Lrg57LO39UjzR8x4', '2025-02-04 05:31:01.017675'),
('q8b39520fejpg58pbiqk49d3pymvobzb', 'eyJsb2dpbklkIjo4fQ:1tauP8:i2vn2kXPRhLe_rQXtdwJt8uBITpKabjvr9oaweGKyBc', '2025-02-06 10:25:42.843118'),
('wq9ofvz1bzsoh8lyaj5p3jsacfboezb5', 'eyJsb2dpbklkIjo4fQ:1tbDWD:g-qyEOhXmrleuasgOP57HRAoO1viHNEnpu3AK8rbCeA', '2025-02-07 06:50:17.310901'),
('q9prinwt8zwlyq9iyh7y0neqr7ishiwv', 'eyJsb2dpbklkIjo4fQ:1tcKgi:y5aiRWkg10VG8vtktUcWuNfUK0AJHX1xaP6fUoC4U04', '2025-02-10 08:41:44.237710'),
('8lw074ya18pkxrhpcwccd7qvzzywph2n', 'eyJsb2dpbklkIjo2fQ:1tcfM4:ay1ltphtoIkMrTP-FYgPv-P9c_Ezo73HyKkIN3wmkaM', '2025-02-11 06:45:48.141696'),
('e7m8h3d2ofon6yl5msdtnj751tm6rtos', 'eyJsb2dpbklkIjo2fQ:1teoKw:hTaev7j8OFeLBywjXkHp6Fa9ZmrJY_Bwj3xODXL80vM', '2025-02-17 04:45:30.161894'),
('lah7vroquem50l53nhcfzzuctdls8twj', 'eyJsb2dpbklkIjo2fQ:1tetK5:2kedY_rGd1su2X52yVO9Pvzv-w3MrYvC_R-rPIp7Lxs', '2025-02-17 10:04:57.975222'),
('fxxakp4u56ixuh4td7l9up2857akpsrc', 'eyJsb2dpbklkIjo2fQ:1tfF3S:sZpG9MuVysSdiBpANE5junyOvKf8X17qhuB74qPJT1Q', '2025-02-18 09:17:14.017643'),
('sd2h7ph6pg8wqbi9t21jvcr42kzeq8ll', 'eyJsb2dpbklkIjo2fQ:1tfaWP:8VCoI7zRuCDzNEy0XMRYgL4TmF_eBCQFg0VN26DY-DY', '2025-02-19 08:12:33.495418'),
('kouq097dnj6z4fy25pyhiwcst2gwqzl2', 'eyJsb2dpbklkIjo2fQ:1tfuPb:g0Tc2wIhKZJqNyk2QJZ5eSuMp6RNhRBGuouxYH8TIZc', '2025-02-20 05:26:51.562376'),
('gwvsryglld271y6jpe2yhyna316l7qd5', 'eyJsb2dpbklkIjo2fQ:1thhd0:fHzJddlAzXDiM8lHrfuWtXf8giol9yU9LL3YnLpHBkE', '2025-02-25 04:12:06.246732'),
('uh5k8yft6s96o9adc67sign4po15ghke', 'eyJsb2dpbklkIjo2fQ:1thjlF:KvZpoeQ8G2Im3lojmEg3e64wPaGuIpCQAtzxynx_KdY', '2025-02-25 06:28:45.264746'),
('dddxa4fpkjldt62hph1rvpwul4vkfv6x', 'eyJsb2dpbklkIjo2fQ:1thlVp:aEew9nj0G1B-njARYH5G0Bq4p9BT1F0cPYczXCXQ40o', '2025-02-25 08:20:57.350625'),
('326jo94284nrleonuvdcgq1xtd1akred', 'eyJsb2dpbklkIjo2fQ:1ti5Br:SAfU6Oo3C1O_DCC-Hfsdhvl4mQ0fad8MCWJeZen8ZI4', '2025-02-26 05:21:39.928051'),
('5fu48ekbsvubnn6dgrqfx7mn7xha4i4z', 'eyJsb2dpbklkIjo2fQ:1tiUS9:XvPxvQnz5yIM1GhjRG40G0Wm3TuO6yfenXjjsBeo8DA', '2025-02-27 08:20:09.341891'),
('16bdyfug8jgydncfd0h6bi3byvhxyqai', 'eyJsb2dpbklkIjo2fQ:1tjBK0:xDUoR6K6T40FDtrgr9ZOaJ-C1C2t9B0m8Dcgj3D5o24', '2025-03-01 06:06:36.788761'),
('bvftljncf1ra7vlt5tg4y2c2lqfj9agx', 'eyJsb2dpbklkIjo2fQ:1tkK9F:OHrSlAyy8p8hnmsCFTYF_S9YFPXe5BnT2AYS8JZlAjw', '2025-03-04 09:44:13.605839'),
('ezrewhvonimrig126plwb985kn2xojld', 'eyJsb2dpbklkIjo2fQ:1tmRTc:Gq6O7D-6DmZq1Aki4FWJI_kI2FKqKa-z0uVTr6RlljU', '2025-03-10 05:58:00.254899'),
('4lkcyc8amr9argx019d6wvzn9yq0n2wq', 'eyJsb2dpbklkIjo2fQ:1tmoU7:WuLRwJgvtIEn3iLwXFaJ5FvjlaoFEXs_3BmNoHgMsX8', '2025-03-11 06:32:03.573644'),
('rqglpdmrnha6os7dhcy8z025d7hmte2p', 'eyJsb2dpbklkIjo4fQ:1tmqsy:UIhv_AKC6-BiT5fTPSgmGqiDpkW9Ipqd5cJSx5yhMyI', '2025-03-11 09:05:52.531254'),
('sqipha9kv8ff3eh5whnbbfergdd7glw7', 'eyJsb2dpbklkIjo4fQ:1tmuCc:Xn1T6apRQhYLX4VSZywkrcgKW3whSjaP2E3d7PP1KPw', '2025-03-11 12:38:22.744859'),
('2q5mvyim4qvb2kzxogbbxakd47kl8shh', 'eyJsb2dpbklkIjo5fQ:1tnXnS:jsM14RvnZfnqRu_LYc9VZKX45lqPBd3VH3xPV_t1s20', '2025-03-13 06:55:02.264775'),
('by5q8pknz624sdebbjzgqxke1q26v678', 'eyJsb2dpbklkIjo2fQ:1tnbjf:1EdYrBXGmID1sIac2_ijGb5TVWBycxN764-5Gyy56XA', '2025-03-13 11:07:23.414142'),
('9vamih7d3i1e11gewxis1fz2zpfdf0wm', 'eyJsb2dpbklkIjoxfQ:1tnveC:lIGS_i5TU1gCiAJbUVWgrBv1CH_55ztZWDtDqaxSfto', '2025-03-14 08:23:04.835135'),
('j2co7l3gcfoqsrzb47xpdu22hgcu8wia', 'eyJsb2dpbklkIjoxNH0:1toLSN:4gSujNQXbdMnwwaLEd4R7LVZWOZ1bMC0rj-e-GyYzcE', '2025-03-15 11:56:35.259254'),
('9xtz8brq0ikgwhxcsn4a2i1ljl3yn87v', 'eyJsb2dpbklkIjo2fQ:1toafu:W2jP1XYRilo79xC-Dl63Ce1kJK6_MvhdbYkX9NhKE6w', '2025-03-16 04:11:34.067004'),
('xnfk4em5gx7dhvapfzd27fh0ywz9tu44', 'eyJsb2dpbklkIjo4fQ:1toyod:g23jKzY3Jg09l2R1zotSLM4Dh_0UBc2OATvwi-7R2Sk', '2025-03-17 05:58:11.473906'),
('myjhuv3a6pmv74792u3tz6srjtnqcwsy', 'eyJsb2dpbklkIjoxfQ:1tpA5p:60RJc030GIC-aX16ZjBfFMYCUu1XWqz8w16G5t6l2u0', '2025-03-17 18:00:41.905512'),
('ye5831ae4pvgabnqo5kl6suny93dospg', 'eyJsb2dpbklkIjo4fQ:1tpJDX:icYZkINpk0OJA_Oipibq7YuVNi6yJZGursZ7vYtI5Ao', '2025-03-18 03:45:15.151222'),
('v6j4kpb2ph9h5yljkoyxw1i166yy9hdk', 'eyJsb2dpbklkIjo4fQ:1tpLxP:Dan1Zon5eP_yrEDLTC8SspKEfxAzRVUwVRtig7YcHe8', '2025-03-18 06:40:47.018298'),
('0e2g9q7eowtp96p7mdx1o6h3lb8g9c6t', 'eyJsb2dpbklkIjo2fQ:1tpM9n:Lv7Z6F56PmR5bTiOAJQoCbHTho9rT2tHSGw0qJLBqog', '2025-03-18 06:53:35.484590'),
('dds5eivx1mz0kd78vsyddkf1gpyj9sja', 'eyJsb2dpbklkIjoxfQ:1tpS6G:qiRVO7zDGX6zvrADEB1k1vHAws9dBGZJgZLVZ6lCEaw', '2025-03-18 13:14:20.010751'),
('v3r262jk876faaengtwk14km0pkyjhne', '.eJyrVsrJT8_M80xRsjLUUSpOzclJLcpLzE1VslLyyi9OLchQCEgszVGCSWXmJqaD5PQ9QYxi_cSi_NzEHL2sgtR0uJrU3MTMHKCaLLD-AqB2w8SS3MSSksRsIJGZ45AOUqCXnJ-LMBZkfS0AXqwxXw:1tq7lb:zuKlIHJZ-7b2WHIyTNKLHA-Cy_gUrpD4F-i-X_IO-rE', '2025-03-20 09:43:47.705186'),
('lovw9j0kz6wj8na0321jgz15mve1zyo2', '.eJxFjbEKhDAQRH9FthbF7rCy1cpfGLwlRndNMLlK_HeTA7UZBubNzEHijN36L7WfkgKL8L5BmVoaXGA_FyN-QndkFSZndZ9NqLE7hVSLZ_MwrLCSmOXf96neICpixJrESmcyUE1O39l035wXYjMxZg:1tqR0W:2lCn6qf5WaED1Wxgw9nU4aa1RlEyc67HGfcEzNRir6Y', '2025-03-21 06:16:28.060510'),
('tn2hhnab4t03yjci7hzmb95qgbaj79i6', '.eJxFjbEKhDAQRH9FthbF7rCy1cpfGLwlRndNMLlK_HeTA7UZBubNzEHijN36L7WfkgKL8L5BmVoaXGA_FyN-QndkFSZndZ9NqLE7hVSLZ_MwrLCSmOXf96neICpixJrESmcyUE1O39l035wXYjMxZg:1tqTVH:E71eARe23qMR_1LwPbzCNTJl_o0KYOx34w3LGqtmNPo', '2025-03-21 08:56:23.400928'),
('fwesn9jml8wofuy6f4hfhj6mybx1dx9w', '.eJxFjbEKhDAQRH9FthbF7rCy1cpfGLwlRndNMLlK_HeTA7UZBubNzEHijN36L7WfkgKL8L5BmVoaXGA_FyN-QndkFSZndZ9NqLE7hVSLZ_MwrLCSmOXf96neICpixJrESmcyUE1O39l035wXYjMxZg:1tqTtT:8GCbG7ErLYw7AytPVK__6m555S8EUdel3r239Fna0gw', '2025-03-21 09:21:23.586034'),
('okjfueo716qa9qh2phsjzzaou1b88rcm', '.eJyrVsrJT8_M80xRsjLUUSpOzclJLcpLzE1VslLyyi9OLchQCEgszVGCSWXmJqaD5PQ9QYxi_cSi_NzEHL2sgtR0uJrU3MTMHKCaLLD-AqB2w8SS3MSSksRsIJGZ45AOUqCXnJ-LMBZkfS0AXqwxXw:1tqZTB:v-Uv6EP_EdMDqKChUn7skCGqtmErUZQGyHIMxLmFMeA', '2025-03-21 15:18:37.585369'),
('paxg9nuhipof5o1k8bgx3n5dwlx97rty', '.eJyrVsrJT8_M80xRsjLUUSpOzclJLcpLzE1VslLyyi9OLchQCEgszVGCSWXmJqaD5PQ9QYxi_cSi_NzEHL2sgtR0uJrU3MTMHKCaLLD-AqB2w8SS3MSSksRsIJGZ45AOUqCXnJ-LMBZkfS0AXqwxXw:1trWxM:qsGfAwwGGsnwlNI3n7a6sa_a-lm2zRmJTP4ivY5w_5E', '2025-03-24 06:49:44.557839'),
('i8apjonlylspdtd7z4a5b607yw49ijly', '.eJxFjbEKhDAQRH9FthbF7rCy1cpfGLwlRndNMLlK_HeTA7UZBubNzEHijN36L7WfkgKL8L5BmVoaXGA_FyN-QndkFSZndZ9NqLE7hVSLZ_MwrLCSmOXf96neICpixJrESmcyUE1O39l035wXYjMxZg:1trx2G:icJO3yr-52VuhqIbAjQ3JHY2LI3Z8py7k4Z-GM54zsg', '2025-03-25 10:40:32.952281'),
('xk99xlae47s1bvv4cvl7na4544e8nyym', 'e30:1tsFRt:OS3YmX6UHNecd6gH-bhNKd4B2ep5O4IZUgFSt4iIV5o', '2025-03-26 06:20:13.022163'),
('dt40wjmmb5t7frhdesww1tk4lrzc5aj8', 'eyJsb2dpbklkIjo2fQ:1tsaVx:i7sooXUg81QYOkhcldl1bsNMNzKM2ObqgKJwAJbAxx4', '2025-03-27 04:49:49.554466'),
('aol3pzrw95sw5mbo7bziuslbkvodschh', 'eyJsb2dpbklkIjoxfQ:1tsfNk:5eBrQFDUyKln0tZyFKXiOA6VhddMpJdc8tRiPAwnHss', '2025-03-27 10:01:40.296546'),
('pq60595dq46g2f0vlo4p1k2b257ubrne', '.eJxFjbEKhDAQRH9FthbF7rCy1cpfGLwlRndNMLlK_HeTA7UZBubNzEHijN36L7WfkgKL8L5BmVoaXGA_FyN-QndkFSZndZ9NqLE7hVSLZ_MwrLCSmOXf96neICpixJrESmcyUE1O39l035wXYjMxZg:1tuDyG:ooFfGAZ6OQ3n1WfDDCw_gAVGdqv6NWonxZZuSN-3UkY', '2025-03-31 17:09:48.164104'),
('sh4he7gbcn6tp7fo87aaskj1f8qmr48o', '.eJxFjbEKhDAQRH9FthbF7rCy1cpfGLwlRndNMLlK_HeTA7UZBubNzEHijN36L7WfkgKL8L5BmVoaXGA_FyN-QndkFSZndZ9NqLE7hVSLZ_MwrLCSmOXf96neICpixJrESmcyUE1O39l035wXYjMxZg:1tuT6h:O3JlgbYbfZ1oUelr5AoptDglMiAQuMYaB2i7vYy9eNA', '2025-04-01 09:19:31.112583'),
('ash7toefovizp3hkv4y60mxjajftph1k', 'eyJsb2dpbklkIjo2fQ:1tuZQF:EoWUGy8EgesXUNPTI3DW6BS37VWBQFkhysG74p71BDo', '2025-04-01 16:04:07.443617'),
('43w50622m7s0806thjlcakwg2b3ty05v', 'eyJsb2dpbklkIjo2fQ:1tv84J:1seqHCka8KUFBhKG7Zr2Fl5eTTMl_Hor8qxzHGdO1TE', '2025-04-03 05:03:47.208618'),
('j0cpjnedxy56tlwumcym913ehwdueik6', 'eyJsb2dpbklkIjoxfQ:1tvdyL:d8e7ZqBPSRZyj4Y3EjAKe4yi0NYcGWtwB-_2TjdRtec', '2025-04-04 15:07:45.679774'),
('kfy91x2oi6fnxt8zdw2p7e5c4s8dwflz', 'e30:1tvfAc:9Rx45vgmsg29ap0erBj99caTTTD5loG2CrOGYUgNuM8', '2025-04-04 16:24:30.317824'),
('mn53pz5p9lb4g73o6iyaw09k3577bp9g', 'e30:1u77oQ:b8rdG3xNhqW_RQr8UpdFX3c0oxX35PvsGS6r82JRHHg', '2025-05-06 07:12:58.964257'),
('glymzm7oxxy1s2pc9rk6w3dp35jm0a1s', 'eyJsb2dpbklkIjo2fQ:1u7XxI:_axnyawvkFuTApPygtyFIkC3X8GjJJB0X2wzcUdjygU', '2025-05-07 11:07:52.608223');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_login`
--

DROP TABLE IF EXISTS `guestapp_tbl_login`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` varchar(25) NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_login`
--

INSERT INTO `guestapp_tbl_login` (`loginid`, `username`, `password`, `role`, `status`) VALUES
(1, 'admin', 'admin', 'admin', 'Accepted'),
(2, 'guest', 'guest', 'user', 'confirmed'),
(6, 'Joseph123', 'Joseph123', 'user', 'confirmed'),
(8, 'josephseller1', 'josephseller1', 'seller', 'Accepted'),
(9, 'jibinseller', 'jibinseller', 'seller', 'Accepted'),
(13, 'phlipseller', 'phlipseller', 'seller', 'Requested'),
(14, 'Kiranseller', 'Kiranseller', 'seller', 'Accepted'),
(15, 'smithaseller', 'smithaseller', 'user', 'confirmed'),
(16, '', '', 'seller', 'Requested'),
(17, 'Danil123', 'Danil123', 'user', 'confirmed'),
(18, 'CharlsSeller', 'CharlsSeller', 'seller', 'Requested'),
(19, 'Kiran123', 'Kiran123', 'user', 'confirmed'),
(20, 'nija', '2EadRJZg', 'user', 'confirmed'),
(21, 'susitha', '', 'seller', 'Requested'),
(24, 'Jacobseller123', 'Jacobseller123', 'seller', 'Accepted'),
(25, 'Jacob', 'Jacob', 'user', 'confirmed');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_seller`
--

DROP TABLE IF EXISTS `guestapp_tbl_seller`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_seller` (
  `seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_name` varchar(25) NOT NULL,
  `seller_image` varchar(100) NOT NULL,
  `seller_phone` bigint(20) NOT NULL,
  `seller_email` varchar(60) NOT NULL,
  `seller_landmark` varchar(40) NOT NULL,
  `seller_pincode` bigint(20) NOT NULL,
  `seller_idproof` varchar(100) NOT NULL,
  `seller_regdate` date NOT NULL,
  `seller_location_id` int(11) NOT NULL,
  `seller_loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`seller_id`),
  KEY `GuestApp_tbl_seller_seller_location_id_41b00711` (`seller_location_id`),
  KEY `GuestApp_tbl_seller_seller_loginid_id_1a9f2347` (`seller_loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_seller`
--

INSERT INTO `guestapp_tbl_seller` (`seller_id`, `seller_name`, `seller_image`, `seller_phone`, `seller_email`, `seller_landmark`, `seller_pincode`, `seller_idproof`, `seller_regdate`, `seller_location_id`, `seller_loginid_id`) VALUES
(1, 'Joseph Paul', 'aromal.jpeg', 852369741, 'josephpaul1atmattakattil@gmail.com', 'Near Heera Cyber Views', 682030, 'aadhaar-card.jpg', '2025-01-23', 1, 8),
(2, 'Jibin Paulson', 'Joseph.jpg', 2583691470, 'jibinpaulson@gmail.com', 'Heera ', 682030, 'aadhaar-card.jpg', '2025-02-27', 1, 9),
(3, 'Phlip', 'aromal.jpeg', 1452369872, 'phlip@gmail.com', 'Heera ', 682030, 'aadhaar-card.jpg', '2025-02-28', 1, 13),
(4, 'Kiram V ', 'rahul.jpeg', 1205489635, 'josephpaulstorage@gmail.com', 'Hill Palace', 682030, 'aadhar.png', '2025-03-01', 1, 14),
(5, 'Charls delvin', 'Screenshot_2023-11-13_102712.png', 1458963257, 'josephpaul200416@gmail.com', 'Santhigiri college', 145236, 'aadhaar-card_yN1qvpV.jpg', '2025-03-13', 5, 18),
(7, 'Jacob Philip', 'Screenshot_2024-01-13_120755_MHdmYGG.png', 8596321472, 'josephpaul1atmattakattil@gmail.com', 'Private bus stand', 683040, 'aadhaar-card_EZ2A0OE.jpg', '2025-04-22', 5, 24);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_user`
--

DROP TABLE IF EXISTS `guestapp_tbl_user`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(25) NOT NULL,
  `user_phone` bigint(20) NOT NULL,
  `user_email` varchar(60) NOT NULL,
  `user_landmark` varchar(40) NOT NULL,
  `user_pincode` bigint(20) NOT NULL,
  `user_regdate` date NOT NULL,
  `user_location_id` int(11) NOT NULL,
  `user_loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `GuestApp_tbl_user_user_location_id_ebb3acb5` (`user_location_id`),
  KEY `GuestApp_tbl_user_user_loginid_id_ccc37fc4` (`user_loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_user`
--

INSERT INTO `guestapp_tbl_user` (`user_id`, `user_name`, `user_phone`, `user_email`, `user_landmark`, `user_pincode`, `user_regdate`, `user_location_id`, `user_loginid_id`) VALUES
(1, 'Joseph Paul', 852369741, 'josephpaul1atmattakattil@gmail.com', 'Heera Cyber Views', 682030, '2025-01-22', 1, 6),
(3, 'Smitha Jibi', 885871228, 'josephpaulstorage@gmail.com', 'OPP Naptol TC', 682030, '2025-03-01', 1, 15),
(4, 'Danil Jose', 9447214229, 'josephpaul200416@gmail.com', 'Santhigiri college', 683040, '2025-03-13', 6, 17),
(5, 'Kiran V Suresh', 1458798987, 'josephpaul200416@gmail.com', 'Private bus stand', 145236, '2025-03-13', 5, 19),
(6, 'nija', 1458798987, 'josephpaul200416@gmail.com', 'Private bus stand', 145236, '2025-03-17', 6, 20),
(7, 'Jacob Philip', 8596321472, 'josephpaul1atmattakattil@gmail.com', 'Private bus stand', 683040, '2025-04-23', 6, 25);

-- --------------------------------------------------------

--
-- Table structure for table `sellerapp_tbl_tool`
--

DROP TABLE IF EXISTS `sellerapp_tbl_tool`;
CREATE TABLE IF NOT EXISTS `sellerapp_tbl_tool` (
  `tool_id` int(11) NOT NULL AUTO_INCREMENT,
  `tool_name` varchar(25) NOT NULL,
  `tool_photo` varchar(100) NOT NULL,
  `tool_price` double NOT NULL,
  `tool_discription` varchar(100) NOT NULL,
  `tool_stock` int(11) NOT NULL,
  `tool_status` varchar(25) NOT NULL,
  `tool_type` varchar(25) NOT NULL,
  `tool_seller_id` int(11) NOT NULL,
  `tool_subcategory_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`tool_id`),
  KEY `SellerApp_tbl_tool_tool_seller_id_be6a960c` (`tool_seller_id`),
  KEY `SellerApp_tbl_tool_tool_subcategory_id_467dc6e7` (`tool_subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sellerapp_tbl_tool`
--

INSERT INTO `sellerapp_tbl_tool` (`tool_id`, `tool_name`, `tool_photo`, `tool_price`, `tool_discription`, `tool_stock`, `tool_status`, `tool_type`, `tool_seller_id`, `tool_subcategory_id`) VALUES
(13, 'Angle cutter', 'Ken_Angle_Grinder.jpg', 4200, 'User for metal works and cutting metal rods', 197, 'Available', 'Rentable', 1, 4),
(12, 'Tool set', 'toolset_bHLRYXQ.jpg', 1200, 'Multiple tools needed for hardware works', 299, 'Available', 'Purchasable', 1, 7),
(14, 'Reciprocating Saw', 'Reciprocating_Saws_6XMQ7TU.jpg', 550, 'Used for PVC and Wood works', 150, 'Available', 'Rentable', 1, 4),
(11, 'Electric Router', '2_Lz2H82W.jpg', 1000, ' Has Straight Guide for Cutting use for wood and metal work', 198, 'Available', 'Rentable', 1, 5),
(7, 'Chainsaw', 'Chainsaw.jpg', 3500, 'Usefull for cutting metal and wood', 198, 'Available', 'Purchasable', 4, 4),
(8, 'Conductivity check kit', 'conductivity_chech_tool_oshTQLj.jpg', 230, 'Used for electrical works', 198, 'Available', 'Purchasable', 4, 8),
(9, 'Lawn Mower', 'lawn_mower_sp.jpg', 60900, 'Used for garden maintenance ', 297, 'Available', 'Purchasable', 4, 4),
(16, 'Construction tool', 'constraction.jpg', 500, 'RIVET BUSTER TOOLS  Chisel Bull Point Ripper RIVET GUN, Air', 200, 'Available', 'Rentable', 7, 7);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_tbl_purchasepayment`
--

DROP TABLE IF EXISTS `userapp_tbl_purchasepayment`;
CREATE TABLE IF NOT EXISTS `userapp_tbl_purchasepayment` (
  `ppayment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ppayment_amount` bigint(20) NOT NULL,
  `ppayment_date` date NOT NULL,
  `ppayment_status` varchar(30) NOT NULL,
  `ppayment_purchaserequestid_id` int(11) NOT NULL,
  `ppayment_userid_id` int(11) NOT NULL,
  PRIMARY KEY (`ppayment_id`),
  KEY `UserApp_tbl_purchasepayment_ppayment_purchaserequestid__14054b6d` (`ppayment_purchaserequestid_id`),
  KEY `UserApp_tbl_purchasepayment_ppayment_userid_id_dace79a8` (`ppayment_userid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_tbl_purchasepayment`
--

INSERT INTO `userapp_tbl_purchasepayment` (`ppayment_id`, `ppayment_amount`, `ppayment_date`, `ppayment_status`, `ppayment_purchaserequestid_id`, `ppayment_userid_id`) VALUES
(1, 3500, '2025-03-03', 'Paid', 1, 1),
(2, 460, '2025-03-03', 'Paid', 2, 1),
(3, 60900, '2025-03-03', 'Paid', 3, 1),
(4, 3500, '2025-03-07', 'Paid', 4, 1),
(5, 1200, '2025-03-07', 'placed', 5, 1),
(6, 121800, '2025-03-17', 'Paid', 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_tbl_purchaserequest`
--

DROP TABLE IF EXISTS `userapp_tbl_purchaserequest`;
CREATE TABLE IF NOT EXISTS `userapp_tbl_purchaserequest` (
  `purchase_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchase_quantity` int(11) NOT NULL,
  `purchase_tprice` bigint(20) NOT NULL,
  `purchase_date` date NOT NULL,
  `purchase_stock` int(11) NOT NULL,
  `purchase_Status` varchar(20) NOT NULL,
  `purchase_toolid_id` int(11) NOT NULL,
  `purchase_userid_id` int(11) NOT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `UserApp_tbl_purchaserequest_purchase_toolid_id_9346e69c` (`purchase_toolid_id`),
  KEY `UserApp_tbl_purchaserequest_purchase_userid_id_ae2323d9` (`purchase_userid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_tbl_purchaserequest`
--

INSERT INTO `userapp_tbl_purchaserequest` (`purchase_id`, `purchase_quantity`, `purchase_tprice`, `purchase_date`, `purchase_stock`, `purchase_Status`, `purchase_toolid_id`, `purchase_userid_id`) VALUES
(1, 1, 3500, '2025-03-03', 199, 'Paid', 7, 1),
(2, 2, 460, '2025-03-03', 198, 'Paid', 8, 1),
(3, 1, 60900, '2025-03-03', 299, 'Paid', 9, 1),
(4, 1, 3500, '2025-03-07', 198, 'Paid', 7, 1),
(5, 1, 1200, '2025-03-07', 299, 'Paid', 12, 1),
(6, 2, 121800, '2025-03-17', 297, 'Paid', 9, 6);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_tbl_rentpayment`
--

DROP TABLE IF EXISTS `userapp_tbl_rentpayment`;
CREATE TABLE IF NOT EXISTS `userapp_tbl_rentpayment` (
  `rpayment_id` int(11) NOT NULL AUTO_INCREMENT,
  `rpayment_amount` bigint(20) NOT NULL,
  `rpayment_date` date NOT NULL,
  `rpayment_status` varchar(30) NOT NULL,
  `rpayment_rentrequestid_id` int(11) NOT NULL,
  `rpayment_userid_id` int(11) NOT NULL,
  PRIMARY KEY (`rpayment_id`),
  KEY `UserApp_tbl_rentepayment_rpayment_rentrequestid_id_5efe7bdd` (`rpayment_rentrequestid_id`),
  KEY `UserApp_tbl_rentepayment_rpayment_userid_id_3ef78187` (`rpayment_userid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_tbl_rentpayment`
--

INSERT INTO `userapp_tbl_rentpayment` (`rpayment_id`, `rpayment_amount`, `rpayment_date`, `rpayment_status`, `rpayment_rentrequestid_id`, `rpayment_userid_id`) VALUES
(1, 2000, '2025-03-03', 'Paid', 1, 1),
(2, 4200, '2025-03-17', 'Paid', 6, 6),
(3, 8400, '2025-03-17', 'Returned', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_tbl_rentrequest`
--

DROP TABLE IF EXISTS `userapp_tbl_rentrequest`;
CREATE TABLE IF NOT EXISTS `userapp_tbl_rentrequest` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_quantity` int(11) NOT NULL,
  `request_tprice` bigint(20) NOT NULL,
  `request_date` date NOT NULL,
  `request_requireddate` date NOT NULL,
  `request_returndate` date NOT NULL,
  `request_Remark` varchar(100) DEFAULT NULL,
  `request_Status` varchar(20) NOT NULL,
  `request_toolid_id` int(11) NOT NULL,
  `request_userid_id` int(11) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `UserApp_tbl_rentrequest_request_toolid_id_b5086b20` (`request_toolid_id`),
  KEY `UserApp_tbl_rentrequest_request_userid_id_cab12db7` (`request_userid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_tbl_rentrequest`
--

INSERT INTO `userapp_tbl_rentrequest` (`request_id`, `request_quantity`, `request_tprice`, `request_date`, `request_requireddate`, `request_returndate`, `request_Remark`, `request_Status`, `request_toolid_id`, `request_userid_id`) VALUES
(1, 2, 2000, '2025-03-02', '2025-03-05', '2025-04-15', 'NULL', 'Accepted', 11, 1),
(2, 2, 8400, '2025-03-03', '2025-03-04', '2025-03-24', 'NULL', 'Accepted', 13, 1),
(3, 2, 1100, '2025-03-03', '2025-03-06', '2025-03-31', 'NULL', 'Requested', 14, 1),
(4, 3, 12600, '2025-03-07', '2025-03-08', '2025-03-29', 'NULL', 'Requested', 13, 1),
(5, 1, 4200, '2025-03-17', '2025-03-17', '2025-03-31', 'NULL', 'Requested', 13, 6),
(6, 1, 4200, '2025-03-17', '2025-03-18', '2025-03-21', 'NULL', 'Accepted', 13, 6);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
