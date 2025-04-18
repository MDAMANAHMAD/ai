//spare programming
public class MaxDistanceCalculator {
    public static int maxDistance(int c, int e, int w) {
        int max = 0;
        for (int f = 1; f <= c; f++) {
            int r = c - f;
            int d = f * e;
            if (r >= w) d += (r - w) * e;
            max = Math.max(max, d);
        }
        return max;
    }

    public static void main(String[] args) {
        int dist = maxDistance(10, 20, 2);
        System.out.println("Maximum distance: " + dist + " miles");
    }
}
