import unittest
from ai_expander import SemanticExpander

class TestSemanticExpander(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.expander = SemanticExpander()
        
    def test_basic_expansion(self):
        """Test basic term expansion."""
        # Test with a known location
        result = self.expander.expand("NYC")
        self.assertIn("New York", result)
        self.assertIn("New York City", result)
        
    def test_case_insensitivity(self):
        """Test that expansion is case-insensitive."""
        result1 = self.expander.expand("nyc")
        result2 = self.expander.expand("NYC")
        self.assertEqual(result1, result2)
        
    def test_custom_mapping(self):
        """Test with custom mappings."""
        custom_mapping = {
            "boston": ["Beantown", "The Hub"],
            "miami": ["Magic City", "The 305"]
        }
        expander = SemanticExpander(custom_mapping=custom_mapping)
        
        result = expander.expand("boston")
        self.assertIn("Beantown", result)
        self.assertIn("The Hub", result)
        
    def test_add_mapping(self):
        """Test adding a new mapping."""
        self.expander.add_mapping("austin", ["ATX", "Live Music Capital"])
        result = self.expander.expand("austin")
        self.assertIn("ATX", result)
        self.assertIn("Live Music Capital", result)
        
    def test_empty_term(self):
        """Test with empty input."""
        result = self.expander.expand("")
        self.assertEqual(result, set())

if __name__ == "__main__":
    unittest.main()
