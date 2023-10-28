-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 28 oct. 2023 à 03:31
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
-- Structure de la table `exam`
--

CREATE TABLE `exam` (
  `ID` int(11) NOT NULL,
  `Groupe` varchar(20) NOT NULL,
  `Classroom` varchar(20) NOT NULL,
  `Proffesseur` varchar(30) NOT NULL,
  `Date` varchar(10) NOT NULL,
  `Time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `exam`
--

INSERT INTO `exam` (`ID`, `Groupe`, `Classroom`, `Proffesseur`, `Date`, `Time`) VALUES
(1, 'B', 'Matiban', 'taiboni', '05/12/2023', '10:30 AM'),
(2, 'A', 'Matiban', 'Taiboni', '27/12/2023', '12:00 PM'),
(3, 'C', 'Hegiene', 'Abbas', '14/12/2023', '9:00 AM');

-- --------------------------------------------------------

--
-- Structure de la table `library`
--

CREATE TABLE `library` (
  `ID` int(11) NOT NULL,
  `Fistname` varchar(20) NOT NULL,
  `Lastname` varchar(20) NOT NULL,
  `Phone` int(10) NOT NULL,
  `Name_book` varchar(20) NOT NULL,
  `Delivry_date` varchar(10) NOT NULL,
  `Return_date` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `library`
--

INSERT INTO `library` (`ID`, `Fistname`, `Lastname`, `Phone`, `Name_book`, `Delivry_date`, `Return_date`) VALUES
(5, 'kuyg', 'oiuh', 674, 'kiuhg', '27/10/2023', '27/11/2023'),
(6, 'bouyemmout', 'meriem', 556091636, 'Python', '27/10/2023', '27/11/2023'),
(7, 'rth', 'trh', 87, 'lkjdfdlsjkh', '27/10/2023', '27/11/2023');

-- --------------------------------------------------------

--
-- Structure de la table `staff`
--

CREATE TABLE `staff` (
  `ID` int(11) NOT NULL,
  `Fistname` varchar(20) NOT NULL,
  `Lastname` varchar(20) NOT NULL,
  `Matricule` int(10) NOT NULL,
  `Job` varchar(30) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Phone` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `staff`
--

INSERT INTO `staff` (`ID`, `Fistname`, `Lastname`, `Matricule`, `Job`, `Email`, `Phone`) VALUES
(1, 'Ayoub', 'Bouyemmout', 2020310291, 'Chef departemment', 'ukyrf', 556019426),
(2, 'jh', 'jhvb', 55, 'Ingénieur', 'kuyt', 3657),
(3, 'lkig', 'kuyt', 3645, 'Secrétère', 'liug', 3573),
(4, 'iuh', 'lh', 354, 'Agent', 'ligh', 3657);

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
(4, 'aaa', 'o', '9582', 'o', 5),
(13, 'o', 'o', '9582', 'o', 5),
(14, 'm', 'm', '7', 'm', 7),
(15, 'h', 'h', '87', 'h', 87),
(16, 'a', 'a', '7', 'a', 52),
(25, 'kjhg', 'kjhg', '54', 'kgh', 354);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `exam`
--
ALTER TABLE `exam`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `library`
--
ALTER TABLE `library`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `exam`
--
ALTER TABLE `exam`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `library`
--
ALTER TABLE `library`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `staff`
--
ALTER TABLE `staff`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `student`
--
ALTER TABLE `student`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
