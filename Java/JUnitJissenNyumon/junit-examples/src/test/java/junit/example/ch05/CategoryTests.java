package junit.example.ch05;

import org.junit.experimental.categories.Categories;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Categories.class)
@Categories.ExcludeCategory(SlowTests.class)
@Suite.SuiteClasses(SlowAndFastTest.class)
public class CategoryTests {
}
