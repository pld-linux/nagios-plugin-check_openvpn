%define		plugin	check_openvpn
Summary:	Nagios plugin to check OpenVPN server status
Name:		nagios-plugin-%{plugin}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://exchange.nagios.org/components/com_mtree/attachment.php?link_id=1459&cf_id=24/check_openvpn.pl
# Source0-md5:	b3f00c6e1a37ec10f41b11609e738c4b
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Security/VPN-Software/check_openvpn_pl/details
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(utils)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
The plugin check_openvpn connects to the management OpenVPN server
checks for active connection and return the amount connected OpenVPN
clients.

%prep
%setup -qcT
%{__sed} -e '
	/diagnostics/d
	s#/usr/nagios/libexec#%{plugindir}#
' %{SOURCE0} > %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
