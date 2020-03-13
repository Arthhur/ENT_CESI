-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 13 mars 2020 à 15:49
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `ent_cesi`
--

-- --------------------------------------------------------

--
-- Structure de la table `article`
--

DROP TABLE IF EXISTS `article`;
CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_publication` date DEFAULT NULL,
  `titre` varchar(30) DEFAULT NULL,
  `contenu` varchar(255) DEFAULT NULL,
  `id_eleve` int(11) NOT NULL,
  `categorie` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `eleve` (`id_eleve`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `article`
--

INSERT INTO `article` (`id`, `date_publication`, `titre`, `contenu`, `id_eleve`, `categorie`) VALUES
(1, '2020-02-08', 'Exposé de groupe', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tempus posuere odio, a imperdiet sem. Suspendisse pharetra sed massa quis pharetra. Proin aliquam tempus ipsum nec condimentum. Integer posuere nulla nisl. Ut non fermentum velit. ', 1, 'pedagogie'),
(2, '2020-01-27', 'Sondage', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tempus posuere odio, a imperdiet sem. Suspendisse pharetra sed massa quis pharetra. Proin aliquam tempus ipsum nec condimentum. Integer posuere nulla nisl. Ut non fermentum velit', 2, 'campus'),
(8, '2020-01-01', 'test', 'test', 1, 'test');

-- --------------------------------------------------------

--
-- Structure de la table `eleve`
--

DROP TABLE IF EXISTS `eleve`;
CREATE TABLE IF NOT EXISTS `eleve` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `url_image` varchar(255) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `promotion_id` int(11) NOT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `promo_eleve` (`promotion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `eleve`
--

INSERT INTO `eleve` (`id`, `nom`, `prenom`, `url_image`, `date_naissance`, `promotion_id`, `mail`, `pwd`) VALUES
(1, 'DUPONT', 'Jean', 'https://resize.prod.docfr.doc-media.fr/r/1010,,forcex/img/var/doctissimo/storage/images/fr/www/beaute/diaporamas/coiffure-homme-coupe-de-cheveux-homme/2763077-11-fre-FR/Coiffure-homme-2019-les-coupes-de-cheveux-pour-hommes-qui-font-craquer-les-filles.jpg', '1990-09-01', 1, 'j.dupont@orange.fr', 'test'),
(2, 'DURANT', 'Marc', 'https://www.olivierdachkin.com/img/cms/coupes-homme/zoom/homme-201708.jpg', '1989-07-05', 2, 'm.durant@yahoo.fr', 'test'),
(3, 'VALJEAN', 'Jean', 'https://compagnieaffable.files.wordpress.com/2015/05/jean-valjean-gc3a9rard-depardieu-les-misc3a9rables.jpg', '1815-12-21', 1, 'jean.valjean@gmail.fr', 'pwd'),
(4, 'KENT', 'Clark', 'https://vignette.wikia.nocookie.net/smallville/images/7/7d/Clark_kent_profile.png/revision/latest?cb=20200124045236', '1980-03-03', 2, 'clark.kent@cesi.fr', 'pwd');

-- --------------------------------------------------------

--
-- Structure de la table `emploi_du_temps`
--

DROP TABLE IF EXISTS `emploi_du_temps`;
CREATE TABLE IF NOT EXISTS `emploi_du_temps` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `libelle` varchar(100) DEFAULT NULL,
  `creneau` varchar(100) DEFAULT NULL,
  `id_promotion` int(11) DEFAULT NULL,
  `id_intervenant` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_promotion` (`id_promotion`),
  KEY `intervenant_promo_edt` (`id_intervenant`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `emploi_du_temps`
--

INSERT INTO `emploi_du_temps` (`id`, `date`, `libelle`, `creneau`, `id_promotion`, `id_intervenant`) VALUES
(1, '2020-03-13', 'Python', '8:45 - 12:15', 1, 1),
(2, '2020-03-13', 'Python', '13:30 - 17:00', 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `intervenant`
--

DROP TABLE IF EXISTS `intervenant`;
CREATE TABLE IF NOT EXISTS `intervenant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `url_photo` varchar(255) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `intervenant`
--

INSERT INTO `intervenant` (`id`, `nom`, `prenom`, `date_naissance`, `url_photo`, `mail`, `pwd`) VALUES
(1, 'CHAN', 'Jacky', '1965-09-24', 'https://victor-mochere.com/wp-content/uploads/2019/02/Best-quotes-from-Jackie-Chan.jpg', 'j.chan@wanadoo.fr', 'test');

-- --------------------------------------------------------

--
-- Structure de la table `promotion`
--

DROP TABLE IF EXISTS `promotion`;
CREATE TABLE IF NOT EXISTS `promotion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL,
  `libelle` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `promotion`
--

INSERT INTO `promotion` (`id`, `date_debut`, `date_fin`, `libelle`) VALUES
(1, '2018-09-01', '2020-08-01', 'RIL'),
(2, '2018-09-01', '2020-09-01', 'RISR');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `eleve` FOREIGN KEY (`id_eleve`) REFERENCES `eleve` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `eleve`
--
ALTER TABLE `eleve`
  ADD CONSTRAINT `eleve_promo` FOREIGN KEY (`promotion_id`) REFERENCES `promotion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `emploi_du_temps`
--
ALTER TABLE `emploi_du_temps`
  ADD CONSTRAINT `edt_intervenant` FOREIGN KEY (`id_intervenant`) REFERENCES `intervenant` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `edt_promo` FOREIGN KEY (`id_promotion`) REFERENCES `promotion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
