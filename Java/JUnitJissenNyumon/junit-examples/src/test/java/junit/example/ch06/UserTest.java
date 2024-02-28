package junit.example.ch06;

import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class UserTest {

    public static class InstanceTest {
        @Test
        public void default_constructor() throws Exception {
            User instance = new User();
            assertThat(instance.getName(), is("nobody"));
            assertThat(instance.isAdmin(), is(false));
        }
    }
}
