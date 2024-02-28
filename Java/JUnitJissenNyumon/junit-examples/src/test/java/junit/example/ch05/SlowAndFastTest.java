package junit.example.ch05;

import org.junit.Test;
import org.junit.experimental.categories.Category;

import static org.junit.Assert.fail;

public class SlowAndFastTest {

    @Test
    public void fastTest_01() throws Exception {

    }

    @Test
    @Category(SlowTests.class)
    public void slowTest_01() throws Exception {
        fail();
    }

    @Test
    @Category(SlowTests.class)
    public void slowTest_02() throws Exception {
        fail();
    }
}
