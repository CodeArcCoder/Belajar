// ===== File: Robot.java =====
public class Robot {
    // ===== Atribut =====
    String tipe;
    int tahunPembuatan;

    // ===== Constructor =====
    public Robot(String tipe, int tahunPembuatan) {
        this.tipe = tipe;
        this.tahunPembuatan = tahunPembuatan;
    }

    // ===== Method =====
    // Method untuk berjalan normal
    public void berjalan() {
        System.out.println("Robot tipe " + tipe + " sedang berjalan dengan kecepatan normal.");
    }

    // Method untuk berjalan cepat
    public void jalanCepat() {
        System.out.println("Robot tipe " + tipe + " sedang berjalan dengan cepat!");
    }

    // Method tambahan untuk menampilkan informasi robot
    public void infoRobot() {
        System.out.println("=== Informasi Robot ===");
        System.out.println("Tipe Robot       : " + tipe);
        System.out.println("Tahun Pembuatan  : " + tahunPembuatan);
    }
}
