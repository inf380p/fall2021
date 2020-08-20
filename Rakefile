require 'html/proofer'
require 'rake/testtask'

Rake::TestTask.new do |t|
  t.libs << "test"
  t.test_files = FileList['test/test*.rb']
  t.verbose = true
end


# task :test do
#   # Make sure there are no baseurls
#   sh 'echo "\n\nbaseurl:\nurl:" >> _config.yml'
#   begin
#     sh "bundle exec jekyll build"
#   rescue Exception => e
#     puts e.message
#     puts e.backtrace.inspect
#     # Remove empty baseurls
#     sh 'head -n -4 _config.yml > tmp && mv tmp _config.yml'
#     raise "build failed"
#   end
#   begin
#     HTML::Proofer.new("./_site", {
#       :disable_external => true,
#       :checks_to_ignore => ['ScriptCheck'],
#       :empty_alt_ignore => true,
#       :verbose => true,
#       :href_ignore => ["#"]
#     }).run
#   rescue Exception => e
#     puts e.message
#     puts e.backtrace.inspect
#   ensure
#     # Remove empty baseurls
#     sh 'head -n -3 _config.yml > tmp && mv tmp _config.yml'
#   end
# end
