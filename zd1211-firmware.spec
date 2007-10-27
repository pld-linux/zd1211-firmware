Summary:	Firmware for the ZyDAS ZD1211 802.11b/g USB WLAN
Summary(pl.UTF-8):	Firmware dla kart sieciowych WLAN ZyDAS ZD1211 802.11b/g USB
Name:		zd1211-firmware
Version:	1.4
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	http://dl.sourceforge.net/zd1211/%{name}-%{version}.tar.bz2
# Source0-md5:	19f28781d76569af8551c9d11294c870
URL:		http://zd1211.ath.cx/
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

install zd* $RPM_BUILD_ROOT/lib/firmware/zd1211

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
/lib/firmware/zd1211
