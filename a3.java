public class WaterJug {
    public static boolean canMeasureWater(int a, int b, int target) {
        return target % gcd(a, b) == 0 && target <= Math.max(a, b);
    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void main(String[] args) {
        int jug1 = 3, jug2 = 5, target = 4;
        System.out.println(canMeasureWater(jug1, jug2, target) 
            ? "Possible" : "Not Possible");
    }
}
