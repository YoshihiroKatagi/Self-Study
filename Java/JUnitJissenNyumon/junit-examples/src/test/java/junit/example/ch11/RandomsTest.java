//package junit.example.ch11;
//
//import org.junit.Test;
//
//import java.util.ArrayList;
//import java.util.List;
//
//import static com.sun.org.apache.xerces.internal.util.PropertyState.is;
//import static org.hamcrest.CoreMatchers.*;
//import static org.junit.Assert.*;
//
//public class RandomsTest {
//
//    @Test
//    public void choice_returns_A() throws Exception {
//        List<String> options = new ArrayList<String>();
//        options.add("A");
//        options.add("B");
//        Randoms sut = new Randoms();
//
//        sut.generator = new RandomNumberGenerator() {
//            @Override
//            public int nextInt() {
//                return 0;
//            }
//        };
//        assertThat(sut.choice(options), is("A"));
//    }
//
//    @Test
//    public void choice_returns_B() throws Exception {
//        List<String> options = new ArrayList<>();
//        options.add("A");
//        options.add("B");
//        Randoms sut = new Randoms();
//
//        sut.generator = new RandomNumberGenerator() {
//            @Override
//            public int nextInt() {
//                return 1;
//            }
//        };
//        assertThat(sut.choice(options), is("B"));
//    }
//}
