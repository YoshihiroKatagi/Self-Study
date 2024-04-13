package junit.example.ch09;

import org.junit.Before;
import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.Verifier;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class VerifierExampleTest {

    @Rule
    public Verifier verifier = new Verifier() {
        protected void verify() throws Throwable {
            assertThat("value should be 0.", sut.value, is(0));
        }
    };

    VerifierExample sut;

    @Before
    public void setUp() throws Exception {
        sut = new VerifierExample();
    }

    @Ignore("後処理としてsut.set(0)を実行していないため、テストは失敗する")
    @Test
    public void get_result_by_getValue() throws Exception {
        sut.set(200);
        sut.add(100);
        sut.minus(50);
        int actual = sut.getValue();
        assertThat(actual, is(250));
    }
}
