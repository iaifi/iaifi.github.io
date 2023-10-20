require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => '.html', :ignore_status_codes => [999], :ignore_missing_alt => true, :empty_alt_ignore => true, :disable_external => true, :enforce_https => false}
  HTMLProofer.check_directory('_site/', options).run
end
