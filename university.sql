-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 21 oct. 2023 à 19:03
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `university`
--

-- --------------------------------------------------------

--
-- Structure de la table `student`
--

CREATE TABLE `student` (
  `ID` int(11) NOT NULL,
  `Fistname` varchar(30) NOT NULL,
  `Lastname` varchar(30) NOT NULL,
  `Matricule` varchar(10) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `student`
--

INSERT INTO `student` (`ID`, `Fistname`, `Lastname`, `Matricule`, `Email`, `Phone`) VALUES
(1, 'Bouyemmout', 'Meriem', '2020310291', 'meriembt7@gmail.com', 556091636),
(2, 'Bouyemmout', 'Hadjer', '2020310654', 'hadjerbt7@gmail.com', 563214789),
(3, 'rhreg', 'rthdrt', '53232', 'eufh', 321420),
(4, 'o', 'o', '9582', 'o', 5),
(13, 'o', 'o', '9582', 'o', 5),
(14, 'm', 'm', '7', 'm', 7),
(15, 'h', 'h', '87', 'h', 87),
(16, 'a', 'a', '7', 'a', 7),
(17, 'b', 'b', '4', 'b', 4),
(18, 'c', 'c', '8', 'c', 4),
(19, 'n', 'n', '6', 'n', 2),
(20, 'jj', 'jj', '7', 'jjj', 77);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `student`
--
ALTER TABLE `student`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
