require 'test/unit'

class TestFilename < Test::Unit::TestCase


    def test_filenames
        unique_names = Array.new
        Dir.glob('_posts/**/*') do |item|
            next if File.directory? item
            filename = File.basename(item)
            assert_match(/^20[12]\d-[01]\d-[3210]\d-[a-zA-Z0-9_-]*\.md$/, filename, "Filename #{item} not valid" )
            html_filename = filename[11..-1]

            path = File.dirname(item)
            next if path.include?("exercise") || path.include?("readings")
            assert(not(unique_names.include? html_filename), "Filename #{html_filename} is not unique.")
            unique_names << html_filename
        end
    end
end