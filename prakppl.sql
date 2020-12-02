-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Nov 2020 pada 14.33
-- Versi server: 10.4.16-MariaDB
-- Versi PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prakppl`
--

DELIMITER $$
--
-- Prosedur
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `SearchPosting` (`Search` VARCHAR(30))  BEGIN
SELECT * FROM posting WHERE posting.Judul LIKE Search;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `AID` int(11) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`AID`, `Nama`, `Password`) VALUES
(1, 'havid', 'havid'),
(2, 'mattoriq', 'mattoriq'),
(3, 'khoirul', 'khoirul');

-- --------------------------------------------------------

--
-- Struktur dari tabel `feedback`
--

CREATE TABLE `feedback` (
  `FID` int(11) NOT NULL,
  `Judul` varchar(50) NOT NULL,
  `Keterangan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `feedback`
--

INSERT INTO `feedback` (`FID`, `Judul`, `Keterangan`) VALUES
(1, 'informasinya tidak lengkap', 'informasi yang disediakan oleh aplikasi mengenai buah apel kurang lengkap tentang kandungan yang didalamnya'),
(2, 'Kurang Menarik', 'penampilan terlalu simpel dan kurang menarik'),
(3, 'salah deskripsi', 'saya mencari isi kandungan buah'),
(4, 'penjelasan ambigu', 'deskripsi cara push up terlalu membingungkan untuk dilakukan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `posting`
--

CREATE TABLE `posting` (
  `PID` int(11) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `type` tinyint(4) NOT NULL,
  `isi` varchar(255) NOT NULL,
  `tanggal` date NOT NULL,
  `admin` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `posting`
--

INSERT INTO `posting` (`PID`, `judul`, `type`, `isi`, `tanggal`, `admin`) VALUES
(1, 'Push Up Tembok', 1, '1.Berdirilah di depan tembok atau dinding yang datar,\r\n2.Kemudian letakkan telapak tangan diatas dinding tersebut\r\n3.Lalu bengkokkan lengan tangan anda dengan gerakan memajukan badan ke area dinding, dan kemudian meluruskan lengan lagi.\r\n4.Kerjakan cara i', '2020-11-26', 'havid'),
(2, 'Push up ', 1, '1.Letakkan kedua tangan anda diatas lantai\r\n2.Bagian Kaki anda bertumpu pada ujung jari kaki sampai posisi tubuh anda lurus\r\n3.Turunkan bagian bahu secara lurus sampai membentuk siku 90 derajat dan kemudian luruskan kembai', '2020-11-26', 'mattoriq'),
(3, 'Apel', 0, 'Buah apel biasanya berwarna merah kulitnya jika masak dan (siap dimakan), namun bisa juga kulitnya berwarna hijau atau kuning. Kulit buahnya agak lembek, daging buahnya keras. Buah ini memiliki beberapa biji di dalamnya.', '2020-11-11', 'khoirul'),
(4, 'Push up Berlutut', 1, '1.Posisikan bentuk tubuh kita seperti halnya Push up yang sebenarnya, namun jika anda menggunakan cara ini gunakan lutut anda sebagai tempat untuk tumpuannya.\r\n2.Kemudian letakkan tangan kita di atas lantai secara lurus wajah kedepan lalu kaki di silangka', '2020-11-26', 'mattoriq'),
(5, 'Jeruk Nipis', 0, 'Buah bulat sampai bulat telur, berwarna hijau sampai kuning dan kulit buah tipis mengandung banyak minyak atsiri. Daging buah berwarna putih kehijauan, sangat asam, mengandung banyak vitamin C dan asam sitrat.', '2020-11-11', 'khoirul'),
(6, 'Hamburger', 0, 'adalah sejenis makanan berupa roti berbentuk bundar yang diiris dua dan di tengahnya diisi dengan patty yang biasanya diambil dari daging, kemudian sayur-sayuran berupa selada, tomat dan bawang bombay. Sebagai sausnya, burger diberi berbagai jenis saus se', '2020-11-12', 'havid'),
(7, 'Buah Naga', 0, 'Buah naga merah sebagai salah satu buah yang memiliki banyak manfaat untuk membantu mengatasi dan membantu menyembuhkan berbagai penyakit. Mulai dari batang buah naga, daging buah naga, sampai dengan kulit buah naga juga memiliki banyak kandungan vitamin ', '2020-11-11', 'khoirul'),
(8, 'Pizza', 0, 'hidangan gurih dari Italia sejenis adonan bundar dan pipih, yang dipanggang di oven dan biasanya dilumuri saus tomat serta keju dengan bahan makanan tambahan lainnya yang bisa dipilih. Keju yang dipakai biasanya mozzarella atau \"keju pizza\", bisa juga kej', '2020-11-12', 'havid'),
(9, 'Melon', 0, 'Beberapa jenis kandungan nutrisi yang terkandung dalam melon termasuk kalium, asam folat, protein, beta-karoten, dan magnesium. Melon juga merupakan satu di antara sumber vitamin, seperti vitamin A, vitamin C, vitamin E, dan vitamin K.', '2020-11-12', 'khoirul'),
(10, 'Soto', 0, 'Soto, sroto, sauto, tauto, atau coto adalah makanan khas Indonesia seperti sop yang terbuat dari kaldu daging dan sayuran. Daging yang paling sering digunakan adalah daging sapi dan ayam, tetapi ada pula yang menggunakan daging babi atau kambing', '2020-11-12', 'mattoriq'),
(11, 'Pull Up', 1, '1.Pegang bar pull up dengan telapak tangan menghadap kedepan\r\n2.Pegang bar pull up dengan telapak tangan menghadap kedepan\r\n3.Turunkan badan kamu sampai tangan kamu hampir terentang secara penuh\r\n', '2020-11-12', 'khoirul');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `UID` int(11) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Usia` varchar(20) NOT NULL,
  `TanggalLahir` date NOT NULL,
  `JenisKelamin` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`UID`, `Nama`, `Usia`, `TanggalLahir`, `JenisKelamin`) VALUES
(1, 'John', '21', '1999-01-01', 0),
(2, 'Adam', '14', '2005-04-01', 0),
(3, 'Siti', '18', '2002-05-01', 1),
(4, 'Budi', '19', '2001-06-04', 0),
(5, 'Maryam', '18', '2002-05-06', 1),
(6, 'Annisa', '19', '2001-06-01', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`AID`);

--
-- Indeks untuk tabel `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`FID`);

--
-- Indeks untuk tabel `posting`
--
ALTER TABLE `posting`
  ADD PRIMARY KEY (`PID`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `AID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `feedback`
--
ALTER TABLE `feedback`
  MODIFY `FID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `posting`
--
ALTER TABLE `posting`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `UID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
