%define		plugin	check_openvpn
Summary:	Nagios plugin to check OpenVPN server status
Name:		nagios-plugin-%{plugin}
Version:	0.1
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://exchange.nagios.org/components/com_mtree/attachment.php?link_id=158&cf_id=24&/check_openvpn
# Source0-md5:	238f7b64955a7cb070b8a9379dbf57bb
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Security/VPN-Software/check_openvpn/details
BuildRequires:	rpm-pythonprov
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
The plugin check_openvpn connects to the management OpenVPN server
checks for active connection and return the amount connected OpenVPN
clients.

%prep
%setup -qcT
%{__sed} -e '1s,^#!.*python,#!%{__python},' %{SOURCE0} > %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
