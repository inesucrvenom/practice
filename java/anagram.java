/*
Provjeravam da je multiskup prve riječi isti kao i multiskup druge. Multiskup je skup koji može imati duplikate. 
Java nema takvu kolekciju, no može poslužiti Map tj. njegova implementacija HashMap, gdje ćemo u vrijednost 
spremati broj ponavljanja pojedinog znaka (ključa)
Svaku riječ treba pretvoriti u takav HashMap i nakon toga ih treba usporediti, postoji metoda equals na Map, 
koja uspoređuje i ključeve i vrijednosti pa ne moramo mi ‘na ruke’ to raditi.
Ad hoc implementacija, izgleda mi malo čupavo i vjerojatno ne najbrže :)

*/
import java.util.Map;
import java.util.HashMap;

public class HelloWorld{

    public static Map transform(String input){
        Map <String, Integer> resultMap = new HashMap<String, Integer>();
        Integer count;
        String key;
        for(char c : input.toCharArray()) {
            key = Character.toString(c);
            count = resultMap.get(key);
            if (count == null){
               count = 1; 
            } else {
                count++;
            }
            resultMap.put(key, count);
        }
        return resultMap;
    }

     public static void main(String []args){
        System.out.println("muzika kuzima " 
        + transform("muzika").equals(transform("kuzima")));
        
        System.out.println("pile lipa " 
        + transform("pile").equals(transform("lipa")));
     }
}
