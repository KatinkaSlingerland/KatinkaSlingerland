package day3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Rucksack {
    public static void main(String[] args) throws IOException {
        final InputStream inStream = Rucksack.class.getResourceAsStream("input.txt");
        try (BufferedReader br =
                     new BufferedReader(new InputStreamReader(inStream, StandardCharsets.UTF_8))) {
            final List<Integer> sommen = new ArrayList<>();
            String line;
            int som = 0;
            List<String> dubbelen = new ArrayList<>();

            int numberOfLines=0;

            while ((line = br.readLine()) != null) {
                String[] compartiment1;
                String[] compartiment2;
                numberOfLines ++;

                compartiment1 = line.substring(0, line.length() / 2).split("");
                compartiment2 = line.substring(line.length() / 2).split("");

                OUTER_LOOP:
                for (String item : compartiment1) {
                    for (String item2 : compartiment2) {
                        if (item.equals(item2)) {
                            dubbelen.add(item);
                            break OUTER_LOOP;
                        }
                    }
                }
            }

            for (String dubbele : dubbelen) {
                System.out.println(dubbele);
                char c = dubbele.charAt(0);
                if ((int) c > 96) {
                    int getal = (int) c - 96;
                    System.out.println(getal);
                    som += getal;

                } else {
                    int getal = (int) c - 38;
                    System.out.println(getal);
                    som += getal;
                }
            }
            System.out.println(som);
        }
    }
}
