drop schema `analytics`;
CREATE SCHEMA `analytics` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

CREATE TABLE `analytics`.`events` (
  `idevents` INT NOT NULL AUTO_INCREMENT,
  `android_id` VARCHAR(45) NULL,
  `app_package_name` VARCHAR(45) NULL,
  `app_version_name` VARCHAR(45) NULL,
  `appmetrica_device_id` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `connection_type` VARCHAR(45) NULL,
  `country_iso_code` VARCHAR(45) NULL,
  `device_locale` VARCHAR(45) NULL,
  `device_manufacturer` VARCHAR(45) NULL,
  `device_model` VARCHAR(45) NULL,
  `device_type` VARCHAR(45) NULL,
  `event_datetime` DATETIME NULL,
  `event_json` VARCHAR(1000) NULL,
  `event_name` VARCHAR(45) NULL,
  `event_receive_datetime` DATETIME NULL,
  `event_receive_timestamp` INT(11) NULL,
  `event_timestamp` VARCHAR(45) NULL,
  `google_aid` VARCHAR(45) NULL,
  `ios_ifa` VARCHAR(45) NULL,
  `ios_ifv` VARCHAR(45) NULL,
  `mcc` INT(3) NULL,
  `mnc` INT(3) NULL,
  `operator_name` VARCHAR(45) NULL,
  `os_name` VARCHAR(45) NULL,
  `os_version` VARCHAR(45) NULL,
  PRIMARY KEY (`idevents`));

  CREATE TABLE `analytics`.`errors` (
  `iderror` INT NOT NULL AUTO_INCREMENT,
  `android_id` VARCHAR(45) NULL,
  `app_package_name` VARCHAR(45) NULL,
  `app_version_name` VARCHAR(45) NULL,
  `appmetrica_device_id` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `connection_type` VARCHAR(45) NULL,
  `country_iso_code` VARCHAR(45) NULL,
  `device_locale` VARCHAR(45) NULL,
  `device_manufacturer` VARCHAR(45) NULL,
  `device_model` VARCHAR(255) NULL,
  `device_type` VARCHAR(45) NULL,
  `error_datetime` DATETIME NULL,
  `error` VARCHAR(10000) NULL,
  `error_id` VARCHAR(45) NULL,
  `error_receive_datetime` DATETIME NULL,
  `error_receive_timestamp` INT(11) NULL,
  `error_timestamp` VARCHAR(45) NULL,
  `google_aid` VARCHAR(45) NULL,
  `ios_ifa` VARCHAR(45) NULL,
  `ios_ifv` VARCHAR(45) NULL,
  `mcc` INT(3) NULL,
  `mnc` INT(3) NULL,
  `operator_name` VARCHAR(45) NULL,
  `os_name` VARCHAR(45) NULL,
  `os_version` VARCHAR(45) NULL,
  `windows_aid` VARCHAR(45) NULL,
  PRIMARY KEY (`iderror`));

  CREATE TABLE `analytics`.`installations` (
  `idinstallation` INT NOT NULL AUTO_INCREMENT,
  `android_id` VARCHAR(45) NULL,
  `app_package_name` VARCHAR(45) NULL,
  `app_version_name` VARCHAR(45) NULL,
  `appmetrica_device_id` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `connection_type` VARCHAR(45) NULL,
  `country_iso_code` VARCHAR(45) NULL,
  `device_locale` VARCHAR(45) NULL,
  `device_manufacturer` VARCHAR(255) NULL,
  `device_model` VARCHAR(255) NULL,
  `device_type` VARCHAR(45) NULL,
  `match_type` VARCHAR(45) NULL,
  `is_reinstallation` VARCHAR(45) NULL,
  `install_receive_timestamp` VARCHAR(45) NULL,
  `install_timestamp` VARCHAR(45) NULL,
  `install_ipv6` VARCHAR(45) NULL,
  `install_datetime` DATETIME NULL,
  `install_receive_datetime` DATETIME NULL,
  `click_datetime` DATETIME NULL,
  `click_ipv6` VARCHAR(1000) NULL,
  `click_id` VARCHAR(45) NULL,
  `click_user_agent` VARCHAR(45) NULL,
  `click_url_parameters` VARCHAR(11) NULL,
  `click_timestamp` VARCHAR(45) NULL,
  `google_aid` VARCHAR(45) NULL,
  `ios_ifa` VARCHAR(45) NULL,
  `ios_ifv` VARCHAR(45) NULL,
  `mcc` INT(3) NULL,
  `mnc` INT(3) NULL,
  `operator_name` VARCHAR(45) NULL,
  `os_name` VARCHAR(45) NULL,
  `os_version` VARCHAR(45) NULL,
  `tracking_id` INT(45) NULL,
  `tracker_name` VARCHAR(45) NULL,
  `publisher_name` VARCHAR(45) NULL,
  `publisher_id` INT(45) NULL,
  PRIMARY KEY (`idinstallation`));
  
  
    CREATE TABLE `analytics`.`crashes` (
  `idcrashes` INT NOT NULL AUTO_INCREMENT,
  `android_id` VARCHAR(45) NULL,
  `app_package_name` VARCHAR(45) NULL,
  `app_version_name` VARCHAR(45) NULL,
  `appmetrica_device_id` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `connection_type` VARCHAR(45) NULL,
  `country_iso_code` VARCHAR(45) NULL,
  `crash` VARCHAR(1000) NULL,
  `crash_datetime` DATETIME NULL,
  `crash_group_id` int(45) NULL,
  `crash_id` int(45) NULL,
  `crash_receive_datetime` DATETIME NULL,
  `crash_receive_timestamp` int(45) NULL,
  `crash_timestamp` int(45) NULL,
  `device_locale` VARCHAR(45) NULL,
  `device_manufacturer` VARCHAR(255) NULL,
  `device_model` VARCHAR(255) NULL,
  `device_type` VARCHAR(45) NULL,
  `google_aid` VARCHAR(45) NULL,
  `ios_ifa` VARCHAR(45) NULL,
  `ios_ifv` VARCHAR(45) NULL,
  `mcc` INT(3) NULL,
  `mnc` INT(3) NULL,
  `operator_name` VARCHAR(45) NULL,
  `os_name` VARCHAR(45) NULL,
  `os_version` VARCHAR(45) NULL,
  `windows_aid` VARCHAR(45) NULL,
  PRIMARY KEY (`idcrashes`));
  