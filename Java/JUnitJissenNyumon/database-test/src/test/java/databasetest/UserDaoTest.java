package databasetest;

import static databasetest.ITableMatcher.tableOf;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import org.dbunit.dataset.ITable;
import org.dbunit.dataset.xml.FlatXmlDataSetBuilder;
import org.junit.Before;
import org.junit.ClassRule;
import org.junit.Rule;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import java.io.InputStream;
import java.util.List;

@RunWith(Enclosed.class)
public class UserDaoTest {

    public static class InCaseUsersHave2Record {
        @ClassRule
        public static H2DatabaseServer server = new H2UtDatabaseServer();
        @Rule
        public DbUnitTester tester = new UserDaoDbUnitTester("fixtures.xml");
        UserDao sut;

        @Before
        public void setUp() throws Exception {
            this.sut = new UserDao();
        }

        @Test
        public void get_2_record_by_getList() throws Exception {
            // Exercise
            List<String> actual = sut.getList();
            // Verify
            assertThat(actual, is(notNullValue()));
            assertThat(actual.size(), is(2));
            assertThat(actual.get(0), is("Ichiro"));
            assertThat(actual.get(1), is("Jiro"));
        }

        @Test
        public void inserted_1_record_by_insert() throws Exception {
            // Exercise
            sut.insert("Saburou");
            // Verify
            ITable actual = tester.getConnection().createDataSet().getTable("users");
            InputStream expectedIn = getClass().getResourceAsStream("expected.xml");
            ITable expected = new FlatXmlDataSetBuilder().build(expectedIn).getTable("users");
            assertThat(actual, is(tableOf(expected)));
        }
    }

    public static class InCaseNoRecordInUsers {
        @ClassRule
        public static H2DatabaseServer server = new H2UtDatabaseServer();
        @Rule
        public DbUnitTester tester = new UserDaoDbUnitTester("zero_fixtures.xml");

        UserDao sut;

        @Before
        public void setUp() throws Exception {
            this.sut = new UserDao();
        }

        @Test
        public void get_zero_record_by_getList() throws Exception {
            // Exercise
            List<String> actual = sut.getList();
            // Verify
            assertThat(actual, is(notNullValue()));
            assertThat(actual.size(), is(0));
        }

        @Test
        public void inserted_1_record_by_insert() throws Exception {
            // Exercise
            sut.insert("Sirou");
            // Verify
            ITable actual = tester.getConnection().createDataSet().getTable("users");
            InputStream expectedIn = getClass().getResourceAsStream("zero_expected.xml");
            ITable expected = new FlatXmlDataSetBuilder().build(expectedIn).getTable("users");
            assertThat(actual, is(tableOf(expected)));
        }
    }

    static class H2UtDatabaseServer extends H2DatabaseServer {
        public H2UtDatabaseServer() { super("h2", "db", "ut"); }
    }

    static class UserDaoDbUnitTester extends DbUnitTester {
        private final String fixture;
        public UserDaoDbUnitTester(String fixture) {
            super("org.h2.Driver", "jdbc:h2:tcp://localhost/db;SCHEMA=ut", "sa", "", "ut");
            this.fixture = fixture;
        }

        @Override
        protected void before() throws Exception {
            executeQuery("DROP TABLE IF EXISTS users");
            executeQuery("CREATE TABLE uses(id INT AUTO_INCREMENT, name VARCHAR(255))");
        }

        @Override
        protected org.dbunit.dataset.IDataSet createDataSet() throws Exception {
            return new FlatXmlDataSetBuilder().build(getClass().getResourceAsStream(fixture));
        }
    }
}
