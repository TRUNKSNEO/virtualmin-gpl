#!/usr/local/bin/perl
# Actually check quotas

require './virtual-server-lib.pl';
&can_edit_templates() || &error($text{'newquotacheck_ecannot'});
&ReadParse();
&ui_print_unbuffered_header(undef, $text{'newquotacheck_title'}, "");

# Run the checks
&require_useradmin();
$dir = $config{'home_quotas'};
if ($in{'who'} == 0 || $in{'who'} == 2) {
	# Check users
	&$first_print(&text('newquotacheck_udoing', "<tt>$dir</tt>"));
	$out = &quota::quotacheck($dir, 1);
	print "<pre>$out</pre>" if ($out);
	&$second_print($text{'setup_done'});
	}
if ($in{'who'} == 1 || $in{'who'} == 2) {
	# Check groups
	&$first_print(&text('newquotacheck_gdoing', "<tt>$dir</tt>"));
	$out = &quota::quotacheck($dir, 2);
	print "<pre>$out</pre>" if ($out);
	&$second_print($text{'setup_done'});
	}

&run_post_actions();
&webmin_log("quotacheck");
&ui_print_footer("", $text{'index_return'});

