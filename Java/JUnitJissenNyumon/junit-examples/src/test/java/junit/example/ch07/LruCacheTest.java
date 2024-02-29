package junit.example.ch07;

import org.junit.Before;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class LruCacheTest {

    public static class InCaseAAndBAreAdded {
        LruCache<String> sut;

        @Before
        public void setUp() throws Exception {
            sut = new LruCache<String>();
            sut.put("A", "valueA");
            sut.put("B", "valueB");
        }

        @Test
        public void size_is_2() throws Exception {
            assertThat(sut.size(), is(2));
        }

        @Test
        public void get_A_returns_valueA_and_keys_is_BA() throws Exception {
            assertThat(sut.get("A"), is("valueA"));
            assertThat(sut.keys.size(), is(2));
            assertThat(sut.keys.get(0), is("B"));
            assertThat(sut.keys.get(1), is("A"));
        }

        @Test
        public void get_B_returns_valueB_and_keys_is_AB() throws Exception {
            assertThat(sut.get("B"), is("valueB"));
            assertThat(sut.keys.size(), is(2));
            assertThat(sut.keys.get(0), is("A"));
            assertThat(sut.keys.get(1), is("B"));
        }

        @Test
        public void get_C_returns_null_and_keys_is_AB() throws Exception {
            assertThat(sut.get("C"), is(nullValue()));
            assertThat(sut.keys.size(), is(2));
            assertThat(sut.keys.get(0), is("A"));
            assertThat(sut.keys.get(1), is("B"));
        }

        @Test
        public void size_is_3_and_keys_is_ABC_by_put_C() throws Exception {
            // SetUp
            String key = "C";
            String item = "valueC";
            // Exercise
            sut.put(key, item);
            // Verify
            assertThat(sut.size(), is(3));
            assertThat(sut.keys.size(), is(3));
            assertThat(sut.keys.get(0), is("A"));
            assertThat(sut.keys.get(1), is("B"));
            assertThat(sut.keys.get(2), is("C"));
        }
    }
}
