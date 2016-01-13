Name:           python-rpm-macros
Version:        3
Release:        4%{?dist}
Summary:        The unversioned Python RPM macros

License:        MIT
Source0:        macros.python
Source1:        macros.python-srpm
Source2:        macros.python2
Source3:        macros.python3

BuildArch:      noarch
Obsoletes:      python-macros < 3
Provides:       python-macros = %{version}-%{release}

%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python-srpm-macros
Summary:        RPM macros for building Python source packages

%description -n python-srpm-macros
RPM macros for building Python source packages.

%package -n python2-rpm-macros
Summary:        RPM macros for building Python 2 packages
# Would need to be different for each release - worth it?
#Conflicts:      python2-devel < 2.7.11-3

%description -n python2-rpm-macros
RPM macros for building Python 2 packages.

%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
# Would need to be different for each release - worth it?
#Conflicts:      python3-devel < 3.5.1-3

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.


%prep

%build

%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -m 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} \
  %{buildroot}/%{_rpmconfigdir}/macros.d/

 
%files
%{_rpmconfigdir}/macros.d/macros.python

%files -n python-srpm-macros
%{_rpmconfigdir}/macros.d/macros.python-srpm

%files -n python2-rpm-macros
%{_rpmconfigdir}/macros.d/macros.python2

%files -n python3-rpm-macros
%{_rpmconfigdir}/macros.d/macros.python3


%changelog
* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> 3-4
- Fix python2/3-rpm-macros package names

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> 3-3
- Add empty %%prep and %%build

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> 3-2
- Combined package

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> 3-1
- Initial package
