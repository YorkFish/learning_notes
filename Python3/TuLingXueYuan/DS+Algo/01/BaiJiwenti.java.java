public class BaiJiwenti {
    // javac -encoding UTF-8 BaiJiwenti.java
    public static void main(String[] args) {
        buy_chicken();
    }

    public static void buy_chicken() {
        for (int x=0; x<20; x++) {
            for (int y=0; y<33; y++) {
                int z = 100 - x - y;
                if (z % 3 == 0 && (x*5 + y*3 + z/3 == 100 )) {
                    System.out.printf("百钱可买公鸡 %2d 只，母鸡 %2d 只，小鸡 %d 只\n", x, y, z);
                }
            }
        }
    }
}
