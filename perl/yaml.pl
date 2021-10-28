use YAML qw(LoadFile);
use Data::Dumper;

my $data = LoadFile($ARGV[0]);
print Dumper($data);
