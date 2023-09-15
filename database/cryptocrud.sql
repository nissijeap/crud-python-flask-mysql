-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2023 at 04:12 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cryptocrud`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES
(1, 'admin', 'password', 'admin@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `cryptocurrency_prices`
--

CREATE TABLE `cryptocurrency_prices` (
  `id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `price_date` date DEFAULT NULL,
  `cryptotype` int(11) DEFAULT NULL,
  `open_price` decimal(12,6) DEFAULT NULL,
  `highest_price` decimal(12,6) DEFAULT NULL,
  `lowest_price` decimal(12,6) DEFAULT NULL,
  `close_price` decimal(12,6) DEFAULT NULL,
  `adjusted_close_price` decimal(12,6) DEFAULT NULL,
  `volume` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cryptocurrency_prices`
--

INSERT INTO `cryptocurrency_prices` (`id`, `created_at`, `price_date`, `cryptotype`, `open_price`, `highest_price`, `lowest_price`, `close_price`, `adjusted_close_price`, `volume`) VALUES
(1, '2023-09-13 11:43:50', '2014-09-19', 48, 424.102997, 427.834991, 384.532013, 394.795990, 394.795990, 37919700),
(2, '2023-09-13 11:44:23', '2014-09-20', 48, 394.673004, 423.295990, 389.882996, 408.903992, 408.903992, 36863600),
(3, '2023-09-13 12:11:54', '2014-02-18', 48, 456.859985, 456.859985, 413.104004, 424.440002, 424.440002, 34483200),
(4, '2023-09-13 12:12:24', '2014-09-21', 48, 408.084991, 412.425995, 393.181000, 398.821014, 398.821014, 26580100),
(5, '2023-09-13 12:12:59', '2014-09-22', 48, 399.100006, 406.915985, 397.130005, 402.152008, 402.152008, 24127600),
(6, '2023-09-13 12:13:30', '2014-09-23', 48, 402.092010, 441.557007, 396.196991, 435.790985, 435.790985, 45099500),
(7, '2023-09-13 12:13:58', '2014-09-24', 48, 435.751007, 436.112000, 436.112000, 423.204987, 423.204987, 30627700);

-- --------------------------------------------------------

--
-- Table structure for table `cryptocurrency_types`
--

CREATE TABLE `cryptocurrency_types` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `symbol` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cryptocurrency_types`
--

INSERT INTO `cryptocurrency_types` (`id`, `name`, `symbol`) VALUES
(1, 'Aave', 'AAVE'),
(2, 'Cardano', 'ADA'),
(3, 'Cosmos', 'ATOM'),
(4, 'Avalanche', 'AVAX'),
(5, 'Basic Attention Token', 'BAT'),
(6, 'Bitcoin Cash', 'BCH'),
(7, 'Binance Coin', 'BNB'),
(8, 'Bitcoin SV', 'BSV'),
(9, 'Compound', 'COMP'),
(10, 'Dai', 'DAI'),
(11, 'Dash', 'DASH'),
(12, 'Dogecoin', 'DOGE'),
(13, 'Polkadot', 'DOT'),
(14, 'Enjin Coin', 'ENJ'),
(15, 'EOS', 'EOS'),
(16, 'Ethereum Classic', 'ETC'),
(17, 'Ethereum', 'ETH'),
(18, 'Filecoin', 'FIL'),
(19, 'IoTeX', 'IOTX'),
(20, 'Chainlink', 'LINK'),
(21, 'Lisk', 'LSK'),
(22, 'Litecoin', 'LTC'),
(23, 'Terra', 'LUNA'),
(24, 'Polygon', 'MATIC'),
(25, 'IOTA', 'MIOTA'),
(26, 'Maker', 'MKR'),
(27, 'Navcoin', 'NAV'),
(28, 'Neo', 'NEO'),
(29, 'Namecoin', 'NMC'),
(30, 'OMG Network', 'OMG'),
(31, 'Peercoin', 'PPC'),
(32, 'Reddcoin', 'RDD'),
(33, 'Ravencoin', 'RVN'),
(34, 'Solana', 'SOL'),
(35, 'Steem', 'STEEM'),
(36, 'THETA', 'THETA'),
(37, 'TRON', 'TRX'),
(38, 'Uniswap', 'UNI'),
(39, 'USD Coin', 'USDC'),
(40, 'Tether', 'USDT'),
(41, 'Stellar', 'XLM'),
(42, 'Monero', 'XMR'),
(43, 'Nano', 'XNO'),
(44, 'Primecoin', 'XPM'),
(45, 'Ripple', 'XRP'),
(46, 'Tezos', 'XTZ'),
(47, 'Zcash', 'ZEC'),
(48, 'Bitcoin', 'BTC'),
(49, 'Binance USD', 'BUSD'),
(50, 'Shiba Inu USD', 'SHIB-USD'),
(51, 'Shiba Inu', 'SHIB');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cryptocurrency_prices`
--
ALTER TABLE `cryptocurrency_prices`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_cryptotype` (`cryptotype`);

--
-- Indexes for table `cryptocurrency_types`
--
ALTER TABLE `cryptocurrency_types`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `cryptocurrency_prices`
--
ALTER TABLE `cryptocurrency_prices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `cryptocurrency_types`
--
ALTER TABLE `cryptocurrency_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cryptocurrency_prices`
--
ALTER TABLE `cryptocurrency_prices`
  ADD CONSTRAINT `fk_cryptotype` FOREIGN KEY (`cryptotype`) REFERENCES `cryptocurrency_types` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
