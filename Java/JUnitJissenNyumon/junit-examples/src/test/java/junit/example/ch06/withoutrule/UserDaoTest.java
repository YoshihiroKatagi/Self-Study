package junit.example.ch06.withoutrule;

import junit.example.ch06.UserDao;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class UserDaoTest {
    private UserDao sut;
    private InMemoryDB db;

    @Before
    public void setUp() throws Exception {
        db = new InMemoryDB();
        db.start();
        sut = new UserDao();
    }

    @After
    public void tearDown() throws Exception {
        db.shutdownNow();
    }

    @Test
    public void getList_returns_0() throws Exception {

    }
}
