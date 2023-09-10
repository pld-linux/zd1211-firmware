Summary:	Firmware for the ZyDAS ZD1211 802.11b/g USB WLAN
Summary(pl.UTF-8):	Firmware dla kart sieciowych WLAN ZyDAS ZD1211 802.11b/g USB
Name:		zd1211-firmware
Version:	1.5
Release:	1
License:	GPL v2
Group:		Base/Kernel
Source0:	https://downloads.sourceforge.net/zd1211/%{name}-%{version}.tar.bz2
# Source0-md5:	3c182ceb9b2fc1d8442cd81c1280d83f
URL:		https://sourceforge.net/projects/zd1211/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware for the ZyDAS ZD1211 802.11b/g USB WLAN cards.

%description -l pl.UTF-8
Firmware dla kart sieciowych WLAN ZyDAS ZD1211 802.11b/g USB.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/zd1211

cp -p zd* $RPM_BUILD_ROOT/lib/firmware/zd1211

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
/lib/firmware/zd1211
