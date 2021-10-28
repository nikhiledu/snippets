#!/usr/bin/perl
#
use Digest::SHA1;
use MIME::Base64;
$ctx = Digest::SHA1->new;
$ctx->add('fffff');
$ctx->add("\xc9\x97\xf0\x83");
$hashedPasswd = '{SSHA}' . encode_base64($ctx->digest .  "\xc9\x97\xf0\x83" ,'');
print 'userPassword: ' .  $hashedPasswd . "\n";

