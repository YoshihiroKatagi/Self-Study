package junit.example.ch06;

import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import java.util.List;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class UserDaoTest {

    public static class InCaseTableIsEmpty {
        UserDao sut;

        @Before
        public void setUp() throws Exception {
            DbUtils.drop("users");
            sut = new UserDao();
        }

        @Ignore("未実装")
        @Test
        public void get_0_data_by_getList() throws Exception {
            List<User> actual = sut.getList();
            assertThat(actual, is(notNullValue()));
            assertThat(actual.size(), is(0));
        }
    }

    public static class InCaseTableContains100SampleData {
        UserDao sut;

        @Before
        public void setUp() throws Exception {
            DbUtils.drop("users");
            DbUtils.insert("users", getClass().getResource("users.yaml"));
            sut = new UserDao();
        }

        @Ignore("未実装")
        @Test
        public void get_100_data_by_getList() throws Exception {
            List<User> actual = sut.getList();
            assertThat(actual, is(notNullValue()));
            assertThat(actual.size(), is(100));
        }
    }
}
