// ===== File: Main.java =====
public class Main1 {
    public static void main(String[] args) {
        // Membuat objek robot baru
        Robot r1 = new Robot("Explorer-X", 2024);
        Robot r2 = new Robot("Guardian-Z", 2020);

        // Menampilkan informasi robot
        r1.infoRobot();
        r1.berjalan();
        r1.jalanCepat();

        System.out.println(); // baris kosong untuk pemisah

        r2.infoRobot();
        r2.berjalan();
        r2.jalanCepat();
    }
}
