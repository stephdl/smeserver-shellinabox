%define name smeserver-shellinabox
%define version 0.0.7
%define release 2
Summary: shellinabox is an ajax webbase terminal
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Distribution: SME Server
License: GNU GPL version 2
Group: SMEserver/addon
Source: smeserver-shellinabox-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}-buildroot
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 9.0
Requires: shellinabox >= 2.14
AutoReqProv: no

%description
 shellinabox is an ajax web based terminal 

%changelog
* Sun Jan 10 2016 stephane de labrusse <stephdl@de-labrusse.fr> 0.0.7-1.sme
- Restrict the deamon to localhost and disable ssl

* Thu Jun 25 2013  stephane de labrusse <stephdl@de-labrusse.fr> 0.0.6-1.sme
- initial release

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
     > %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre

%post



