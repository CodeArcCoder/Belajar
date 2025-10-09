public class Function {
    // 1) Method tanpa parameter dan tanpa return
    public static void tampilkanSalam() {
        System.out.println("Halo! Ini method tanpa parameter dan tanpa return.");
    }

    // 2) Method dengan parameter (tanpa return)
    public static void sapaOrang(String nama) {
        System.out.println("Halo, " + nama + "! Senang bertemu denganmu.");
    }

    // Method utama (main)
    public static void main(String[] args) {
        // Memanggil method tanpa parameter
        tampilkanSalam();

        // Memanggil method dengan parameter
        sapaOrang("Evan");
        sapaOrang("Rehan");
    }
}
