package junit.example.ch06.rule;

import junit.example.ch06.UserDao;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;

public class UserDaoTest {
    private UserDao sut;

    @Rule
    public InMemoryDBRule db = new InMemoryDBRule();

    @Before
    public void setUp() throws Exception {
        sut = new UserDao();
    }

    @Test
    public void getList_returns_0() throws Exception {

    }
}
